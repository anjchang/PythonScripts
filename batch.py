import os,sys
#path="../AngelasXoomTest3/";
#path="."/
path="T:/SecondPass/wonchi/1/edu.mit.media.funf.bgcollector/";
files = os.listdir(path);
for i in files:
    f = path + i;
    if (f.find(".db") >= 0) and (f.find("orig") < 0):
        os.system("python ./dbdecrypt1.py " + f);

