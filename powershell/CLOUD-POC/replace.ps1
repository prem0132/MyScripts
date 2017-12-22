$configFiles = Get-ChildItem ./ appsettings.json -rec
foreach ($file in $configFiles)
{
    (Get-Content $file.PSPath) |
    Foreach-Object { $_ -replace "Data Source=172.16.151.107;UID=test;password=test123;Database=EmployeeMDS;", "Data Source=srvazrpocmgrap1.database.windows.net,1433;UID=rdsadmin;password=Test123#;Database=EmployeeMDS;" } |
    Set-Content $file.PSPath
}