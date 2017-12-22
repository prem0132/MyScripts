##################################################################
# Name             : Windows PowerShell ISE Host
# Version          : 5.1.14393.693
# OS               : Windows Server 2016 Standard Evaluation
# SETTING UP DEPLOYMENT ENVIRONMENT ON WS2016
# MPHASIS LTD. Nov 2017
##################################################################

#Installing Docker Community Edition
#URL needs to be changed for Eterprise Edition
#Docker CE 17.09.0-ce-win33

wget https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe -OutFile $pwd\Dockerinstaller.exe
.\Dockerinstaller.exe

#Docker needs user to log out and log in again to complete the installation
#netplwiz disables password [RESTART]
#work around needed
#can be done manually or should be taken care by any restart

#Installing Kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.8.0/bin/windows/amd64/kubectl.exe
#copy to c:\Windows\System32\

#Can be tweaked to install any other components required for complete environment setup

#.net core 2.0.2 SDK
wget https://download.microsoft.com/download/7/3/A/73A3E4DC-F019-47D1-9951-0453676E059B/dotnet-sdk-2.0.2-win-gs-x64.exe