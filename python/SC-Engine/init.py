#!/usr/bin/python
import requests
import socket

###############CHAIN OF EVENTS###############
def samplegetcall():
    print("This is a Sample get call using hardcoded authentication \n")
    URL = "http://127.0.0.1:5000/redfish/v1/AccountService/"
    r = requests.get(url = URL, auth=('root', 'password123456'))
    print("URL: %s \n"%URL)
    returncode = r.status_code
    print("Headers: %s\n"%(r.headers))
    if(returncode == 200):
        print("GET Call Successful\n")
        print("Status Code: %s\n"%(returncode)) 
        data = r.json()
        print("Data:\n %s\n"%(data))
    else:
        print("GET Call Failed\n")
        print("Status Code: %s\n"%(returncode)) 
    return returncode



################main function###############
def main():
	print("Initiating Smart Component Installation......\n")
	samplegetcall()
	print("The test has completed. Generating log file....")
	print('the test has successfully completed. Please check logs.')



#############calling main function############
if __name__ == "__main__":
	main()
		




		
