for($i=0; $i -lt $args.Count; $i++)
{
   $args[$i] = $args[$i].ToString()
   $dir = $args[$i].Substring(2)
   cd $pwd/$dir/$dir  
   #$tag = "cloudpoc/laas-aks-linux-azure:"+$dir.ToLower() 
   $tag = "cloudpoc2017/laas-aks-linux-azure:"+$dir.ToLower()
   dotnet clean
   dotnet restore
   dotnet build
   dotnet publish -c Release -o ./obj/Docker/publish
   #$imageid = docker images -q $tag
   #Start-process -FilePath 'docker' -ArgumentList {"run -d" $imageid}
   #Start-Process  -FilePath 'dotnet' -ArgumentList 'run'
   docker build -t $tag .
   #docker tag $imageid $tag2
   #docker rmi -f $imageid
   docker push $tag
   #$imageid = docker images -q $tag
   #docker run -d $imageid
   cd ../../
} 

#Script will take directories as argument for context
#restore, build, publish, run locally on IIS
