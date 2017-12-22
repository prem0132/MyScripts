##################################################################
# Name             : Windows PowerShell ISE Host
# Version          : 5.1.14393.693
# OS               : Windows Server 2016 Standard Evaluation
# SETTING UP WINDOWS ENVIRONMENT ON WS2016
# MPHASIS LTD. Nov 2017
##################################################################

# Might have to tweak the file a bit for WIN10
# Powershell 5.1 comes by default in WS2016


#Get-WindowsFeature cmdlet shows all available features. 
#More features can be enabled using the same syntax
#Enabling Hyper-V requires a reboot so script execution will break. 
#Execution Policy must be set for sripts
#Windows Container Feature can also be enabled [Requires Reboot]

Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Confirm:$false
Install-WindowsFeature -Name DNS -LogPath $pwd/logs/dns.log -ErrorAction SilentlyContinue -Confirm:$false
Install-WindowsFeature -Name Hyper-V -LogPath $pwd/logs/hyper-v.log -ErrorAction SilentlyContinue -Confirm:$FALSE -Restart:$false
Install-WindowsFeature -Name Containers -LogPath $pwd/logs/containers.log -ErrorAction SilentlyContinue -Confirm:$FALSE -Restart:$true

