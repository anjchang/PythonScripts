import os, shutil, errno, glob
#copies all the merged tablet data from nested directories off one drive
#to another destination drive
source_base = "./"
key =".db"
dest_base = "F://week4db//"
path = "F://2012-03-08//"
#does not include last number
for dirname in range(20,21):
	sourcedir = path+str(dirname)+"/edu.mit.media.funf.bgcollector"
	destdir = dest_base 
	print sourcedir
	os.chdir(sourcedir);
	files = os.listdir(sourcedir);
	
	for filename in glob.glob("*.db"):
		newfilename = destdir+str(dirname)+"tablet"+filename
		print newfilename
		shutil.copy(filename,  newfilename );
