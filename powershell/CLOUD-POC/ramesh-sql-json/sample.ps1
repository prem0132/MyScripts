
."C:\Users\prem\Desktop\Cloud\ps_scripts\MphPowerShellUtility.ps1"


$jsonFile = "C:\Users\prem\Desktop\Cloud\ps_scripts\DBScript.json"
$Jsonobj = get-content  $jsonFile | Out-String | ConvertFrom-Json

echo jsonobj
echo $Jsonobj

echo jsonobj.txt
$database1 = $jsonobj.service1
echo $database1.DBServerInstancename.value;
echo $database1.database
echo $database1.DatabaseName.value

$configuration= GetJsonObject -jsonFile $jsonFile
$database =$configuration.service2

$DBServer=$database.DBServerInstancename.value;

$DBName=$database.DatabaseName.value
$UserName=$database.SQLUserId.value
$Password=$database.SQLPassword.value

$SqlFolderPath=$database.SQLFolder.value
echo configuration
echo $configuration


echo data
echo $database
echo $DBServer
echo $DBName
echo $UserName
echo $Password
echo $SqlFolderPath

