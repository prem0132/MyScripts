
function GetJsonObject($jsonFile)
{
    try
   {
        $datafileExists = Check-FileExists($jsonFile)

        if ($datafileExists -eq 0)
        {
            $Jsonobj = get-content  $jsonFile | Out-String | ConvertFrom-Json
            return $Jsonobj 
        }
        else
        {
         return -1
        }
    }
    catch
    {
         return $Error[0] 
    }

}

function Check-FileExists($datafile)
{
    try
    {
        $datafileExists = Test-Path $datafile

        if ($datafileExists)
            {
                return 0
            } 
        else 
            {
               return -100
            }
      }

       catch
    {
         return $Error[0] 
    }
    
}

function WriteLog 
{ 
    [CmdletBinding()] 
    Param 
    ( 
        [Parameter(Mandatory=$true)] 
                   
        [ValidateNotNullOrEmpty()] 
        [Alias("LogContent")] 
        [string]$LogMsg, 
    
        [Parameter(Mandatory=$false)] 
        [ValidateSet("Error","Warn","Info")] 
        [string]$MsgLevel="Info", 

        [Parameter(Mandatory=$false)] 
        [string]$configFilePath='C:\Ddata\Ramesh\PowerShellComponent\PowershellComponent.json',

        [Parameter(Mandatory=$false)] 
        [string]$LogFolder,

        [Parameter(Mandatory=$false)] 
        [string]$LogFile

    ) 
 
    Begin 
    { 
        # Set VerbosePreference to Continue so that verbose messages are displayed. 
        $VerbosePreference = 'Continue' 
    } 
    Process 
    { 
        if ( ($LogFolder -eq ' ') -or ($LogFile -eq ' ') ) 
            {
                 $jsonfile = GetJsonObject -jsonFile $configFilePath
                 $LogFilePath =$jsonfile.LogFolder
            }
         else
         {
            if ( ($LogFolder.Length >0) -and ($LogFile.Length>0) )
                {
                    $LogFilePath = $LogFolder +'\'+ $LogFile 
                 }
         }
       
        # If the file already exists and NoClobber was specified, do not write to the log. 
        if ((Test-Path $LogFilePath) )
             { 
            Return -1 
            } 
       
        elseif (!(Test-Path $LogFilePath)) { 
               
                $NewLogFile = New-Item $LogFilePath -Force -ItemType folder 
            } 
 
        else { 
            # Nothing to see here yet. 
            } 
 
        # Format Date for our Log File 
        $FormattedDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss" 
 
        # Write message to error, warning, or verbose pipeline and specify $LevelText 
        switch ($Level) { 
            'Error' { 
                Write-Error $Message 
                $LevelText = 'ERROR:' 
                } 
            'Warn' { 
                Write-Warning $Message 
                $LevelText = 'WARNING:' 
                } 
            'Info' { 
                Write-Verbose $Message 
                $LevelText = 'INFO:' 
                } 
            } 
         
        # Write log entry to $Path 
        "$FormattedDate $LevelText $Message" | Out-File -FilePath $LogFilePath -Append 
    } 
    End 
    { 
    } 
}


