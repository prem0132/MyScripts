#!/usr/bin/python
from logfile import Log

import requests
import os
import json
import sys
import platform


class test:

    logger = Log()
    logger.initiate(platform.system())


    ##############POST CAlL##################
    def uploadfile(self,info,filename,filepath,uri):
        self.logger.add("POST Operation in Progress...")
        self.logger.add("\nUploadFile <%s> <%s>\n"%(filename,info["ip"]))
        URL = "https://"+info["ip"]+uri
        #self.logger.add("\nURL: %s \n"%URL)
        resp = {"headers":"null","status_code":"null","returnifo":{'error': {'@Message.ExtendedInfo': [{'MessageId': 'Connection Refused'}], 'code': 'iLO.0.10.ExtendedInfo', 'message': 'See @Message.ExtendedInfo for more information.'}}}
        files = {'upload_file': open(filepath,'rb')}
        try:
            r = requests.post(url = URL, verify=False, auth=(info["UserName"], info["Password"]),files=files)
            returncode = r.status_code
            headers = r.headers
            returninfo = r.json()
            self.logger.add("################################################")
        except:
            self.logger.add("################################################")
            self.logger.add("\nConnection Refused \n")
            returncode = resp["status_code"]
            headers = resp["headers"]
            returninfo = resp["returnifo"]
        if(returncode == 200):
            self.logger.add("FILE UPLOAD Call Successful\n")
            #self.logger.add("Headers: %s\n"%(headers))
            self.logger.add("Status Code: %s\n"%(returncode)) 
            self.logger.add("Response: %s\n"%(returninfo["error"]['@Message.ExtendedInfo'][0]["MessageId"]))
            #self.logger.add(returninfo)
            self.logger.add("################################################")
        else:
            self.logger.add("FILE UPLOAD Failed\n")
            self.logger.add("Status Code: %s\n"%(returncode))
            self.logger.add("Response: %s\n"%(returninfo["error"]['@Message.ExtendedInfo'][0]["MessageId"]))
            self.logger.add("################################################")
        return returncode
        





    ##############terminste##################
    def terminate():
        self.logger.add("***code for logout****")
        



    ##################BIN FUNC###################
    def binfunction(self):
        cwd = os.getcwd()
        #self.logger.add("PRESENT WORKING DIRECTORY:: %s"%(cwd))
        #self.logger.add("SCANNING DIRECTORY....\n")
        for root, dirs, files in os.walk(cwd):
            for file in files:
                if file.endswith(".deb") or file.endswith(".bin") or file.endswith(".tgz"):
                    binfile = file
                    binfilepath = os.path.join(root, file)
        try:
            binfile
            return binfile,binfilepath
        except:
            self.logger.add("NO PAYLOAD FILE FOUND ")
            self.logger.add("EXITING...")
            sys.exit()
        


    ################main function###############
    def getinfo(self):
        if sys.version_info.major == 2:
            #self.logger.add(sys.version_info.major)
            ip = raw_input("\nPlease enter the IP(16.1.1.1):")
            username = raw_input("\nPlease enter the UserName(artik):")
            password = raw_input("\nPlease enter the Password(artik):")
        else:
            #self.logger.add(sys.version_info.major)
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
        self.logger.add("user details:  %s"%(info))
        return info

        
    ################main function###############
    def main(self):
        self.logger.add("Initiating Smart Component Installation......")
        #getting bin file from pwd

        #getting info from user
        info = self.getinfo()

        binfile,binfilepath = self.binfunction()
        self.logger.add("Flashing Bin File: %s "%(binfile))
        #self.logger.add("binfilepath: %s  \n"%(binfilepath))
        postreturn = uploadfile(info,binfile,binfilepath,"/redfish/v1/UpdateService/uploadFile")

    
		




		