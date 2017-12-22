$numbers = (Get-Disk |? OperationalStatus -eq 'online').Number 
$ScriptBlock =
 {
    param($drive_letter, $drive_letters) 
    $files = dir $drive_letters':\'
    foreach($file in $files)
    {
    $var = Get-FileHash $drive_letter$file -Algorithm MD5
    $var1 = ConvertTo-Json -InputObject $var 
    $var1 | Add-Content C:\users\Administrator\Desktop\checksumoutput.json
    }

}
for ($i = 1; $i -le $numbers.Count-1; $i++)
{ 
    $drive_letters = (Get-Partition -DiskNumber $i -PartitionNumber 2).DriveLetter
    $drive_letter = (Get-PSDrive -PSProvider FileSystem -LiteralName $drive_letters ).Root
    Start-Job -ScriptBlock $ScriptBlock -ArgumentList $drive_letter, $drive_letters
}
Wait-Job -State Running