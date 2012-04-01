import os, shutil, errno, glob
#copies all the merged tablet data from nested directories off one drive
#to another destination drive
source_base = "F://ed2//dev.laptop.org//~edmcnierney/"
key ="merged"
dest_base = "Y:/"

for dirname in range(1, 21):
	sourcedir = source_base+str(dirname)+"/edu.mit.media.funf.bgcollector"
	destdir = dest_base +"/"+ str(dirname)
	print destdir
	os.chdir(sourcedir);
	for filename in glob.glob(key+"*"):
		shutil.copy(filename,  destdir );
