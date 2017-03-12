#!/usr/bin/python2

import os, sys, pylab, numpy

def is_black(image):
    """
    Returns True if the argument is a black image, and False
    otherwise.  We check by counting whether less than 4% of pixels
    have a value greater than 30.
    """
    return numpy.average(image > 30) < .04

def list_blacks(directory):
    """
    List jpg files in 'directory' for which is_black() is true.
    """
    result = []
    for dirpath, dirnames, filenames in os.walk(directory):
        print("Scanning {0}".format(dirpath))
        for filename in filenames:
            if filename.lower().endswith('.jpg'):
                path = os.path.join(dirpath, filename)
                try:
                    if is_black(pylab.imread(path)):
                        result.append(path)
                except:
                    print("Error loading {0}".format(path))
    return result

def delete_files(files):
    """
    Delete a list of files, after confirming with the user.
    """
    delete = raw_input("Delete {0} files? [y/N] ".format(len(files)))
    if delete.lower() == 'y':
        for f in files:
            os.remove(f)
        print("Success.")
    else:
        print("Deletion cancelled.")
        
if __name__ == '__main__':
    directory = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    print("Finding black images in {0}".format(directory))
    delete_files(list_blacks(directory))
