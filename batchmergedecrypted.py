#!/usr/bin/python2.7

import os, sys
from dbmerge import merge
def list_files(directory):
    """
    List jpg files in 'directory' for which is_black() is true.
    """
    result = []
    for dirpath, dirnames, filenames in os.walk(directory):
        print("Scanning {0}".format(dirpath))
        for filename in filenames:
            if filename.lower().endswith('.db'):
                path = os.path.join(dirpath, filename)
                try:
                        result.append(path)
                except:
                    print("Error loading {0}".format(path))
    return result

def merge_files(files):
    """
    Decrypt a list of files, after confirming with the user.
    """
    print("merging "+str(files));
    merge(files)
        
if __name__ == '__main__':
    directory = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    print("Finding decrypted files in {0}".format(directory))
    merge_files(list_files(directory))
