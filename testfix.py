import os
import fix_timestamps
file1 = open('test.db','w')
file2 = open('notexist.db','w')
fix_timestamps(file1,file2);
