#!/usr/bin/python
import datetime
import os
import subprocess
import sys
import time

###########getting SUT info###########
def sutinfo():
	server_info = subprocess.check_output("dmidecode -t 1", shell=True)
	chassis_info = subprocess.check_output("dmidecode -t 11", shell=True)
	return server_info, chassis_info

##########Creating Repository#############
def repo(cwd):
	component_list =[]
	component_list_path =[]
	print("SCANNING REPOSITORY....\n")
	for root, dirs, files in os.walk(cwd):
		for file in files:
			if file.endswith(".scexe"):
				component_list.append(file)
				component_list_path.append(os.path.join(root, file))
	return component_list, component_list_path

##############return Component name################
def scname(component_list):
	component_name = []
	print("The Smart Components to be tested are:")
	for component in component_list:
		sc_name = component.split(".")
		component_name.append(sc_name[-2])
		print(sc_name[-2])
	return component_name

###############defining gethelp####################
def gethelp():
	print("usage:")
	print("./SC-Test.py <path to directory> [<run type>optional]")
	print("./SC-Test.py -h for gethelp")
	print("path to directory e.g. /root/Desktop/mydir")
	print("run type -s silent ")
	sys.exit()
	return

#############SETTING PARAMETERS###############
def runmode():
	mode = ''
	if os.path.exists(sys.argv[1]):
		path = sys.argv[1]
		if len(sys.argv) == 2:
			print("interactive  mode")
		elif sys.argv[2] == '-s':
			mode = "-s"
		else:
			gethelp()
	else:
		gethelp()
	return mode, path

################TEMP FILE###################
def tempfile_create():
	mode, path = runmode()
	cwd = os.getcwd()
	logfilepath = sclog(path)
	try:
		os.stat('/var/cpq')
	except:
		os.mkdir('/var/cpq')
	i = 0
	modifytemp(i,path,mode,cwd,logfilepath)
	os.rename('/etc/rc.d/rc.local', '/etc/rc.d/rc.local.jic')
	return
		
##########REBOOT-001#############
def getdata():
	value =  []
	proc = open('/var/cpq/temp.txt', 'r').readlines()
	for line in proc:
		value.append(line.strip())
	component_list, component_list_path = repo(value[1])
	return component_list, component_list_path, value

##################ADD REbOOT #################
def addreboot(log_path):
	time.sleep(5)
	with open(log_path,'a') as logg:
		logg.write("This component was successfully installed \n Please see next log")
	logg.close()
	return
	
###################CREATING SC-TEST-LOG###################
def sclog(path):
	test_time = datetime.datetime.now()
	time_file = test_time.strftime("%Y%m%d%H%M%S")
	a,b = sutinfo()
	file = path +'SC-log-' + time_file + ".txt"
	with open(file,'w') as log:
		log.write("Test start time %s" % test_time)
		log.write('\n\nServer Info: \n%s\n\n'% a)
		log.write('\n\nChassis Info: \n%s\n\n'% b)
	log.close()
	return file

################getting status##############
def getstatus(ret_code):
	if ret_code == 0:
		stats = "PASSED"
	elif ret_code == 2:
		stats = "UP TO DATE"
	elif ret_code == 4:
		stats = "NOT COMPATIBLE"
	elif ret_code == 5:
		stats = "CANCELLED BY USER"
	else:
		stats ="FAILED"
	return stats

#################WRITIN IN THE MAIN LOGFILE#############
def writelog(log_file,log_path,rc,status):
	proc = open(log_file, 'r').readlines()
	with open(log_path,'a') as logg:
		for line in proc:
			if "Installing:" in line:
				logg.write(line.strip()+"\n")
			if "Description:" in line:
				logg.write(line.strip()+"\n")
			if "New Version:" in line:
				logg.write(line)
			if "Current Version:" in line:
				logg.write(line)
		logg.write("Return Code: %s\n"% rc)
		logg.write("Status: %s \n"% status)
	logg.close()
	return

##############getting old log############
def getoldlog():
	if os.path.exists('/var/cpq/Component.log'):
		oldlog = open('/var/cpq/Component.log')
		old_log = oldlog.read()
	else: 
		old_log = ''
	return old_log
	
#############TESTING COMPONENTS###########
def testing(component_list, component_list_path,index, mode,log_path, path):
	test_time = datetime.datetime.now()
	time_file = test_time.strftime("%Y%m%d%H%M%S")
	return_code =[]
	status = []
	comp_name = scname(component_list)
	print("testing.......\n")
	for i in range(int(index),len(component_list)):
		makeexec(component_list_path[i])
		cwd = os.getcwd()
		if i == len(component_list)-1:
			os.remove('/etc/rc.d/rc.local')
			os.rename('/etc/rc.d/rc.local.jic', '/etc/rc.d/rc.local')
			os.remove('/var/cpq/temp.txt')
			subprocess.call('chmod +x /etc/rc.d/rc.local',shell=True)
		else:
			modifytemp(i,path,mode,cwd,log_path)
			addrc(cwd, path)
		with open(log_path,'a') as logg:
			logg.write("\n\n\nComponent under test: %s\n" % comp_name[i])
		logg.close()
		test_comp = component_list_path[i] + mode
		print("Testing Smart Component... ***%s*** \n" % comp_name[i])
		old_log = getoldlog()
		component_install = subprocess.Popen(test_comp,shell=True)
		component_install.wait()
		rc = component_install.returncode
		status = getstatus(rc)
		print("done...\n")
		print("Return Code is %s \n" % rc)
		if rc == 0:
			print("The Smart Component %s flashed successfully.....\n" % comp_name[i]+"\n")
			print("going for iLO reset...wait...\n" )
			time.sleep(90)
		else:
			print("%s flash failed \n" % comp_name[i])
		log_file = createnewcomplog(old_log,comp_name[i],time_file)
		writelog(log_file,log_path,rc,status)
	print("going for next component...\n")
	print("testing function ends")
	return

###############new component log in /var/cpq######
def createnewcomplog(old_log,comp_name,time_file):
	new_log = open('/var/cpq/Component.log').read()	
	log = new_log.replace(old_log,'')
	log_file = '/var/cpq/'+ comp_name +"-"+ time_file + ".txt"
	print("%s log is at %s \n" % (comp_name,log_file))
	with open(log_file,'w') as logger:
		logger.write(log)	
	logger.close()
	return log_file

################MODIFY TEMP#################
def modifytemp(i,path,mode,cwd,logfilepath):
	if os.path.exists('/var/cpq/temp.txt'):
		os.remove('/var/cpq/temp.txt')
	file = '/var/cpq/temp.txt'
	with open(file, 'w') as temp:
		temp.write("%s \n" %i)
		temp.write("%s \n" %path)
		temp.write("%s \n" %mode)
		temp.write("%s \n" %cwd)
		temp.write("%s \n" %logfilepath)
	temp.close()
	return

###########making all .scexe execultable#############
def makeexec(comppath):
	cmd = "chmod +x "+ comppath
	subprocess.call(cmd, shell=True)
	return

###############CHAIN OF EVENTS###############
def chainofevents():
	component_list, component_list_path, value = getdata()
	index = int(value[0])
	log_path = value[4]
	path = value[1]
	mode = value[2]
	if not index == 0:
		addreboot(log_path)
	testing(component_list, component_list_path,index, mode,log_path, path)
	return

#####################ADD RC.LOCAL##################
def addrc(filepath, dirpath):
	if os.path.exists('/etc/rc.d/rc.local'):
		os.remove('/etc/rc.d/rc.local')
	command = 'cd ' + filepath
	command2 = 'gnome-terminal -e python SC-Test.py ' + dirpath 
	with open('/etc/rc.d/rc.local.jic') as fin:
		rclocal = fin.readlines()
		with open('/etc/rc.d/rc.local','w') as fout:
			fout.writelines(rclocal)
			fout.write('\n%s' % command)
			fout.write('\n%s' % command2)
		fout.close()
	fin.close()
	subprocess.call('chmod +x /etc/rc.d/rc.local', shell=True)
	return

################main function###############
def main():
	print("Initiating test......\n")
	if os.path.exists('/var/cpq/temp.txt'):
		print("temp exixts")
		chainofevents()
	else:
		tempfile_create()
		chainofevents()
	print("The test has completed. Generating log file....")
	print('the test has successfully completed. Please check logs.')

#############calling main function############
if __name__ == "__main__":
	main()
		




		
