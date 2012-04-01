import os
import dbmerge 
# merges database already decrypted
path = "X:\\wonchi2\\attemptmerge\\"
mergeList = [f for f in os.listdir(path) if f.find('.db') > 0 and f.find('.orig') == 0]
print mergeList
dbmerge.merge[mergeList,"mergeout.db")
    
        
