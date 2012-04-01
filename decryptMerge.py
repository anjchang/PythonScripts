import os
from dbmerge import merge
# merges database already decrypted
path = "./"
mergeList = [f for f in os.listdir(path) if f.find('.db') > 0 and f.find('.orig') == 0]
print mergeList
merge(mergeList)
    
        
