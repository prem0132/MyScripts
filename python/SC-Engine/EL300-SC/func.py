###############SAMPLE GET CALL###############
def getcall(info,uri):
    self.logger.add("This is a Sample get call using hardcoded authentication \n")
    URL = "https://"+info["ip"]+uri
    self.logger.add("URL: %s \n"%URL)
    r = {"headers":"null","status_code":"null"}
    try:
        r = requests.get(url = URL, verify=False, auth=(info["UserName"], info["Password"]))
        returncode = r.status_code
        headers = r.headers
    except:
        self.logger.add("Connection Refused \n")
        returncode = r["status_code"]
        headers = r["headers"]
    if(returncode == 200):
        self.logger.add("GET Call Successful\n")
        self.logger.add("Headers: %s\n"%(headers))
        self.logger.add("Status Code: %s\n"%(returncode)) 
        info = r.json()
        self.logger.add("response:\n %s\n"%(info))
        self.logger.add("content:\n %s\n"%(r.content))
    else:
        self.logger.add("GET Call Failed\n")
        self.logger.add("Status Code: %s\n"%(returncode)) 
    return returncode



def osinfo(self):
    self.logger.add("OS: %s"%platform.system())


###########def get token#################
def gettoken(info,uri):
    self.logger.add("Generating Token")
    URL = "https://"+info["ip"]+uri
    r = {"headers":"null","status_code":"null"}
    rawdata = {"UserName": info["UserName"],"Password":info["Password"]}
    data = json.dumps(rawdata)
    headers = {'Content-type': 'application/json'}
    self.logger.add("Request Data: \n %s"%(data))
    self.logger.add("URL: %s \n"%URL)
    try:
        r = requests.post(url = URL, verify=False, data = data, headers = headers )
        returncode = r.status_code
        headers = r.headers
    except:
        self.logger.add("Connection Refused \n")
        returncode = r["status_code"]
        headers = r["headers"]
    if(returncode == 200):
        self.logger.add("LOGIN Successful \n")
        self.logger.add("Headers: %s \n"%(headers))
        self.logger.add("X-AUTH-TOKEN: %s \n"%(headers["x-auth-token"]))
        self.logger.add("Status Code: %s\n"%(returncode)) 
        response = r.json()
        self.logger.add("response:\n %s\n"%(response))
        self.logger.add("content:\n %s\n"%(r.content))
    else:
        self.logger.add("LOGIN Failed\n")
        self.logger.add("Status Code: %s\n"%(returncode)) 
    return returncode



    #self.logger.add("################################################")
    #sample get call
    #response = getcall(info,"/redfish/v1/AccountService/")
    #self.logger.add("Response for call: %s \n"%(response))
    #self.logger.add("################################################")
    #generate token
    #token = gettoken(info,"/redfish/v1/Sessions")
    #self.logger.add("################################################")
    #Post File for Upload


    #self.logger.add("################################################")
    #LogOut
    #terminate()
    #self.logger.add('The Smart Component has successfully installed. Please check logs.')