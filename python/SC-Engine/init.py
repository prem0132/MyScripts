#!/usr/bin/python
import requests
import socket

###############CHAIN OF EVENTS###############
def chainofevents():
    print("Welcome to the future\n")
    URL = "http://127.0.0.1:5000/redfish/v1/AccountService/"
    r = requests.get(url = URL, auth=('root', 'password123456'))
    returncode = r.status_code
    print("Headers: %s\n"%(r.headers))
    if(returncode == 200):
        print("GET Call Successful\n")
        data = r.json()
        print("data: %s\n"%(data))
    else:
        print("Status Code: %s\n"%(returncode)) 
    return returncode



################main function###############
def main():
	print("Initiating test......\n")
	chainofevents()
	print("The test has completed. Generating log file....")
	print('the test has successfully completed. Please check logs.')

#############calling main function############
if __name__ == "__main__":
	main()
		




		
