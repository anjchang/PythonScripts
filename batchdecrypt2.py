#!/usr/bin/python2.7

import os, sys


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

def decrypt_files(files):
    """
    Decrypt a list of files, after confirming with the user.
    """
    for eachfile in files:
        print("decrypting "+eachfile);
        os.system("python ./dbdecrypt1.py " + eachfile);
        
if __name__ == '__main__':
    directory = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    print("Finding decrypting files in {0}".format(directory))
    decrypt_files(list_files(directory))
