#!/usr/bin/python
import requests
import os
import json
import sys
import platform

def osinfo():
    print(platform.system())

###############SAMPLE GET CALL###############
def getcall(info,uri):
    print("This is a Sample get call using hardcoded authentication \n")
    URL = "https://"+info["ip"]+uri
    print("URL: %s \n"%URL)
    r = {"headers":"null","status_code":"null"}
    try:
        r = requests.get(url = URL, verify=False, auth=(info["UserName"], info["Password"]))
        returncode = r.status_code
        headers = r.headers
    except:
        print("Connection Refused \n")
        returncode = r["status_code"]
        headers = r["headers"]
    if(returncode == 200):
        print("GET Call Successful\n")
        print("Headers: %s\n"%(headers))
        print("Status Code: %s\n"%(returncode)) 
        info = r.json()
        print("response:\n %s\n"%(info))
        print("content:\n %s\n"%(r.content))
    else:
        print("GET Call Failed\n")
        print("Status Code: %s\n"%(returncode)) 
    return returncode


##############POST CAlL##################
def uploadfile(info,filename,filepath,uri):
    print("POST Operation in Progress...")
    print("\nUploadFile <%s> <%s>\n"%(filename,info["ip"]))
    URL = "https://"+info["ip"]+uri
    #print("\nURL: %s \n"%URL)
    resp = {"headers":"null","status_code":"null","returnifo":{'error': {'@Message.ExtendedInfo': [{'MessageId': 'Connection Refused'}], 'code': 'iLO.0.10.ExtendedInfo', 'message': 'See @Message.ExtendedInfo for more information.'}}}
    files = {'upload_file': open(filepath,'rb')}
    try:
        r = requests.post(url = URL, verify=False, auth=(info["UserName"], info["Password"]),files=files)
        returncode = r.status_code
        headers = r.headers
        returninfo = r.json()
        print("################################################")
    except:
        print("################################################")
        print("\nConnection Refused \n")
        returncode = resp["status_code"]
        headers = resp["headers"]
        returninfo = resp["returnifo"]
    if(returncode == 200):
        print("FILE UPLOAD Call Successful\n")
        #print("Headers: %s\n"%(headers))
        print("Status Code: %s\n"%(returncode)) 
        print("Response: %s\n"%(returninfo["error"]['@Message.ExtendedInfo'][0]["MessageId"]))
        #print(returninfo)
        print("################################################")
    else:
        print("FILE UPLOAD Failed\n")
        print("Status Code: %s\n"%(returncode))
        print("Response: %s\n"%(returninfo["error"]['@Message.ExtendedInfo'][0]["MessageId"]))
        print("################################################")
    return returncode
    


###########def get token#################
def gettoken(info,uri):
    print("Generating Token")
    URL = "https://"+info["ip"]+uri
    r = {"headers":"null","status_code":"null"}
    rawdata = {"UserName": info["UserName"],"Password":info["Password"]}
    data = json.dumps(rawdata)
    headers = {'Content-type': 'application/json'}
    print("Request Data: \n %s"%(data))
    print("URL: %s \n"%URL)
    try:
        r = requests.post(url = URL, verify=False, data = data, headers = headers )
        returncode = r.status_code
        headers = r.headers
    except:
        print("Connection Refused \n")
        returncode = r["status_code"]
        headers = r["headers"]
    if(returncode == 200):
        print("LOGIN Successful \n")
        print("Headers: %s \n"%(headers))
        print("X-AUTH-TOKEN: %s \n"%(headers["x-auth-token"]))
        print("Status Code: %s\n"%(returncode)) 
        response = r.json()
        print("response:\n %s\n"%(response))
        print("content:\n %s\n"%(r.content))
    else:
        print("LOGIN Failed\n")
        print("Status Code: %s\n"%(returncode)) 
    return returncode


##############terminste##################
def terminate():
    print("***code for logout****")
    



##################BIN FUNC###################
def binfunction():
    cwd = os.getcwd()
    #print("PRESENT WORKING DIRECTORY:: %s"%(cwd))
    #print("SCANNING DIRECTORY....\n")
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(".deb") or file.endswith(".bin") or file.endswith(".tgz"):
                binfile = file
                binfilepath = os.path.join(root, file)
    try:
        binfile
        return binfile,binfilepath
    except:
        print("\n NO PAYLOAD FILE FOUND ")
        print("\n EXITING...")
        sys.exit()
    


################main function###############
def getinfo():
    if sys.version_info.major == 2:
        #print(sys.version_info.major)
        ip = raw_input("\nPlease enter the IP(16.1.1.1):")
        username = raw_input("\nPlease enter the UserName(artik):")
        password = raw_input("\nPlease enter the Password(artik):")
    else:
        #print(sys.version_info.major)
        ip = input("\nPlease enter the IP(16.1.1.1):")
        username = input("\nPlease enter the UserName(artik):")
        password = input("\nPlease enter the Password(artik):")
    if ip == '':
        ip = "16.1.1.1"
    if password == '':
        password = "artik"
    if username == '':
        username = "artik"
    info = {"ip":ip,"UserName":username,"Password":password}
    #print("user details: \n %s"%(info))
    return info

    
################main function###############
def main():
    print("\nInitiating Smart Component Installation......")
    #getting bin file from pwd

    #getting info from user
    info = getinfo()
    #print("################################################")
    #sample get call
    #response = getcall(info,"/redfish/v1/AccountService/")
    #print("Response for call: %s \n"%(response))
    #print("################################################")
    #generate token
    #token = gettoken(info,"/redfish/v1/Sessions")
    #print("################################################")
    #Post File for Upload
    binfile,binfilepath = binfunction()
    print("\nFlashing Bin File: %s \n "%(binfile))
    #print("binfilepath: %s  \n"%(binfilepath))
    postreturn = uploadfile(info,binfile,binfilepath,"/redfish/v1/UpdateService/uploadFile")
    #print("################################################")
    #LogOut
    #terminate()
    #print('The Smart Component has successfully installed. Please check logs.')
    



#############calling main function############
if __name__ == "__main__":
	main()
		




		
