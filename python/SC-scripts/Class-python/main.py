from logfile import Log

import platform

def main():
    prem = Log()
    #prem.message = "prem message"
    prem.initiate(platform.system())
    print(prem.add("Test Begins..."))
    print(prem.add("Test Begins 001..."))
    print(prem.add("Test Begins 002..."))
    print(prem.add("Test Begins 003..."))


    
if __name__ == "__main__":  
    main()