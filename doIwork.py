#combine decrypted files from a range of directories labeled 1-20
# merges database already decrypted
import os
from dbmerge import merge
path = "./" 
os.chdir(path);
print "here I am"
for dirname in range(2, 20):
	subpath=  path +str(dirname)+"//edu.mit.media.funf.bgcollector/";
	files = os.listdir(subpath) 
	for eachfile in files:
		filetoanalyze = subpath + eachfile;
		if (filetoanalyze.find(".db") >= 0) and (filetoanalyze.find("orig") < 0):
			os.system("python ./dbmerge.py " + filetoanalyze );
	#mergeList = [f for f in os.listdir(subpath) if f.find('.db')>0]
	
    
print "done"
