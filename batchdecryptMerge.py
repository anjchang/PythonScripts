#combine decrypted files from a range of directories labeled 1-20
# merges database already decrypted
import os
from dbmerge import merge
path = "./" 
os.chdir(path);
print "here I am"
for dirname in range(2, 20):
	subpath=  path +str(dirname)+"//edu.mit.media.funf.bgcollector/";
	#print subpath
	#print os.listdir(subpath)
	#filelist = [f for f in os.listdir(subpath) if f.find('.db') or f.find('.orig')]
	#print filelist
	mergeList = [f for f in os.listdir(subpath) if f.find('.db')>0]
	merge(mergeList)
    
print "done"
