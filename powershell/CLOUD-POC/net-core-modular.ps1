## get help function
function GET_HELP
{
Write-Host "Script takes command line arguments `n 
    Enter flag Value `n
    -a all `n
    -n new templates
    -d dotnet commands `n
    -do docker commands `n
    -iis test on iis `n
    -don run on docker locally `n
    example `n 
    ./script -a laas laascheckin laascheckout `n
    ./script -n laas laascheckin laascheckout `n" 
}

##processing command line
[String]$flag=$args[0]
if(-not $flag.StartsWith("-"))
{
Write-Host "Flag not found `n" -ForegroundColor Red
GET_HELP
}
else
{
Write-Host "Processing Command line...`n" -ForegroundColor Yellow
Write-Host "Fetching Microservices Name..." -ForegroundColor DarkGreen


###########
$microservices = New-Object System.Collections.ArrayList
for($i=0; $i -lt $args.Count; $i++)
    {
		[String]$var = $args[$i]
        if(-not $var.StartsWith("-"))
            {
                [String[]] $microservices += $var
            }
	}
if($microservices.Count -eq 0)
	{
		Write-Host "service names not found" -ForegroundColor Red
	}
		Write-Host $microservices
###########

###########
Write-Host "Fetching flags..." -ForegroundColor DarkGreen
for($i=0; $i -lt $args.Count; $i++)
    {
		[String]$var = $args[$i]
        if($var.StartsWith("-"))
            {
                [String[]] $flags += $var
            }
	}
		Write-Host $flags
############
}

##processing flags
for($i=0; $i -lt $flags.Count; $i++)
{
	for($j=0; $j -lt $microservices.Count; $j++)
		{
			[String]$var = $flags[$i]
			if($var.Equals("-n"))
				{
					Write-Host "Generating Templates..." 
					mkdir $microservices[$j]
					cd $microservices[$j]
					dotnet new webapi
					cd ..
				}
			if($var.Equals("-d"))
				{
					Write-Host "Running dotnet jobs..."
					cd $microservices[$j]
					dotnet build
					dotnet restore
					dotnet publish -c Release -o ./obj/Docker/publish
					cd ..
				}
		}
}
