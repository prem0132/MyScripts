#!/usr/bin/python
import requests
import socket

###############CHAIN OF EVENTS###############
def chainofevents():
    print("Welocme to the future")
    URL = "http://localhost:5000/redfish/v1/Managers/1/"
    r = requests.get(url = URL)
    data = r.json()
    print(data)
    return



################main function###############
def main():
	print("Initiating test......\n")
	chainofevents()
	print("The test has completed. Generating log file....")
	print('the test has successfully completed. Please check logs.')

#############calling main function############
if __name__ == "__main__":
	main()
		




		
