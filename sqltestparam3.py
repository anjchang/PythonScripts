#!/usr/bin/python
# -*- coding: utf-8 -*-
#reads all databases in a directory and looks for parameter
path = "."
import os, glob
import sqlite3 as lite
import sys
files = os.listdir(path);

con = None
for files in glob.glob('*.db'):
    con = lite.connect(files);
    #connection object is returned

    with con:
        cur = con.cursor()    
        #retrieve all the data from the table named "data"
        cur.execute('SELECT * FROM data WHERE name like "LauncherApp" ORDER BY VALUE')
        #return the set of all data
        rows = cur.fetchall()
        for row in rows:
            print row

    
