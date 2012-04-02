#!/usr/bin/python
# -*- coding: utf-8 -*-
#reads the whole database
import sqlite3 as lite
import sys

con = None
#We initialize the con variable to None. In case cannot create a connection to the db
#(e.g disk full) we would not have a connection variable defined. 
#This would lead to an error in the finally clause. 


con = lite.connect('test2.db')
#connection object is returned

with con:
    cur = con.cursor()    
    #retrieve all the data from the table named "data"
    cur.execute('SELECT * FROM data WHERE name like "LauncherApp"')
    #return the set of all data
    rows = cur.fetchall()
    for row in rows:
        print row
    
