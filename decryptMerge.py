import os,sys
from dbmerge import merge
# merges database already decrypted
path = "T:"
print os.listdir(path)
mergeList = [f for f in os.listdir(path) if f.find('.db') > 0 and f.find('.orig') == 0]
print mergeList
merge(mergeList)
    
        
