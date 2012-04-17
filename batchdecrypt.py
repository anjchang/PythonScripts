#Decrypt a batch of files within subdirectories numbered 1-20
import os,sys
path="./";
files = os.listdir(path);
print files
for dirname in range(1, 20):
	subpath = path +str(dirname)+"/edu.mit.media.funf.bgcollector/";
	print subpath
	files = os.listdir(subpath);
	for eachfile in files:
		filetodecrypt = subpath + eachfile;
		print filetodecrypt
		if (filetodecrypt.find(".db") >= 0) and (filetodecrypt.find("orig") < 0):
			os.system("python ./dbdecrypt1.py " + filetodecrypt);

