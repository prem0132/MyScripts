
#param( [Parameter(Mandatory=$true)][string]$PropertyFilePath, [Parameter(Mandatory=$true)][string]$SqlFolderPath)

######including script file - ####



param( [Parameter(Mandatory=$true)][string]$PropertyFilePath)

."C:\Ddata\Ramesh\PowerShellComponent\MphPowerShellUtility.ps1"

#set-executionpolicy remotesigned

#$PropertyFilePath='C:\Ddata\Ramesh\PowerShellComponent\DBScript.json'

#Loading the properties file to read all the properties

$configuration= GetJsonObject -jsonFile $PropertyFilePath

# - end of reading
#Assigning the values for from properties Files
$database =$configuration.database

$DBServer=$database.DBServerInstancename.value;

$DBName=$database.DatabaseName.value
$UserName=$database.SQLUserId.value
$Password=$database.SQLPassword.value

$SqlFolderPath=$database.SQLFolder.value
#$SqlLog=$database.SQLLogPath.value

#Connect to MS SQL Server
try
{
    $SQLConn = New-Object System.Data.SqlClient.SqlConnection
    #Checking for username and password
    if($userName -and $password)
    {
        $SQLConn.ConnectionString = "Server=" + $DBServer + ";Database=" + $DBName + ";User ID= " + $UserName + ";Password=" + $Password + ";"
    }
   else
    {
        #if SQL UserName and Password is not mentioned, will go with Windows Crendetials
        $SQLConn.ConnectionString = "Server=" + $DBServer + ";Database=" + $DBName + ";Integrated Security=True"
    }

    $SQLConn.Open()
}
catch
{
 
   WriteLog  -LogMsg  $Error[0] -MsgLevel "Error" -LogFile 'PowerShellComp_SQL.log'
   
   if ($SQLConn.State -eq [Data.ConnectionState]::Open) {
      $SQLConn.Close()
 }    
   exit 1
}
#loading Sql related module
Import-Module sqlps -DisableNameChecking



foreach ($filename in get-childitem -path $SqlFolderPath -filter "*.sql" )
    {
        WriteLog  -LogMsg  "---------------------------------------------" 
        WriteLog  -LogMsg  "Executed SQL File:" $filename.fullname
        
        try        
        {
           $AnySQLErr = $false
           WriteLog  -LogMsg  "SqlFile:" + $filename.fullname + "stared execution.."
           
           invoke-sqlcmd –ServerInstance $DBServer -Database $DBName -InputFile $filename.fullname
           WriteLog  -LogMsg  $Error[0]
           WriteLog  -LogMsg  "SqlFile:" + $filename.fullname + "execution completed"
        }
        catch
        {
            $AnySQLErr = $true
            WriteLog  -LogMsg  $Error[0]
            WriteLog  -LogMsg  "----------"
        }
        if(-not $AnySQLErr)
        {
            WriteLog  -LogMsg  "Execution successful"
        }
        else
        {
            WriteLog  -LogMsg  "Execution failed"
        }
       
    }

$SQLConn.Close()   #Closing SQL Connection



