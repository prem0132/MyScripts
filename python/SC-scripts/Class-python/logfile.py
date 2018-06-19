import sys
import datetime
import os

class Log:
    
    time = datetime.datetime.now()
    message = "null"
    status =""
    filepath =""
    comp_name ="esc_fw_"
    time_file = time.strftime("%Y%m%d%H%M%S")
    

    def initiate(self,osname):
        print("Creating Log File...")
        if osname == 'Windows':
            print("This is Windows")
            try:
                os.stat('C:\cpqsystem')
            except:
                os.mkdir('C:\cpqsystem')
            self.filepath = "C:\cpqsystem\\" + self.comp_name +"-"+ self.time_file + ".log"
        elif osname == 'Linux':
            print("This is Linux")
            try:
                os.stat('/var/cpq')
            except:
                os.mkdir('/var/cpq')
            self.filepath = '/var/cpq/'+ self.comp_name +"-"+ self.time_file + ".log"
        else:
            print("Unidentified System")
            sys.exit()
        print("Log file at: %s"%(self.filepath))
        with open(self.filepath,'w') as openlog:
            openlog.write("Test start time %s" % self.time)
        openlog.close()
        return self.filepath


    def add(self,message):
        desc_str = "[%s]         %s \n" % (self.time,message)
        with open(self.filepath,'a') as openlog:
            openlog.write(desc_str)
        openlog.close()
        return desc_str


