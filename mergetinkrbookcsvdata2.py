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
            if filename.lower().endswith('tinkrbook.csv'):
                path = os.path.join(dirpath, filename)
                try:
                        result.append(path)
                except:
                    print("Error loading {0}".format(path))
    return result

def merge_csv_files(files):
    count=0
    fout=open("out.csv","a")

    for eachfile in files:
        sourcefile=open(eachfile)
        if count != 0:
            sourcefile.next()
        for line in sourcefile:
            fout.write(line)
            count = count + 1
        sourcefile.close
        #print eachfile 
        #print count
    fout.close()
    #print count


if __name__ == '__main__':
    directory = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    print("Merging csviles in {0}".format(directory))
    merge_csv_files(list_files(directory))
