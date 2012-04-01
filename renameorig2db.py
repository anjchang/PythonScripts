#Enter the direcory 
#batch truncation of the .orig extension 
import glob,os
#path="../AngelasXoomTest3/";
#path="."/
path="T:/SecondPass/wonchi/1/orig/";
os.chdir(path)
for filename in glob.glob("*.orig"):
    newName=".".join(filename.split(".")[:2])
    os.rename(filename,newName);




