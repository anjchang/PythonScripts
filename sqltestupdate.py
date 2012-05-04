#!/usr/bin/python
# -*- coding: utf-8 -*-
#reads the whole database
import sqlite3 as lite
import sys

con = None
#We initialize the con variable to None. In case cannot create a connection to the db
#(e.g disk full) we would not have a connection variable defined. 
#This would lead to an error in the finally clause. 

con = lite.connect('testnew.db')
#connection object is returned

with con:
    cur = con.cursor()    
    print "connection established"

    #retrieve all the data from the table named "data"
    cur.execute('SELECT * FROM data WHERE name like "LauncherApp"')
    #use description
    print(cur.description)
    colnames =  [desc[0] for desc in cur.description]
    print colnames

    #return the set of all data

    rows= cur.fetchall()
    new_rows = []
    for row in rows:
        #update all timestamps > 9000000 to reasonable
        if (row[2]>=9000000):
            new_time=int(row[2]/1000)
       
        cur.execute('UPDATE timestamp SET timestamp=? where timestamp >= ?',[int(row[2]/1000),9000000])
        print row
    print(cur.rowcount)


    
