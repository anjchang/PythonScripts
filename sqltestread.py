#!/usr/bin/python
# -*- coding: utf-8 -*-
#reads the whole database
import sqlite3 as lite
import sys

con = None
#We initialize the con variable to None. In case cannot create a connection to the db
#(e.g disk full) we would not have a connection variable defined. 
#This would lead to an error in the finally clause. 

try:
    con = lite.connect('test2.db')
    #connection object is returned
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    #fetch the data, one record
    
    data = cur.fetchone() 
    print "SQLite version: %s" % data                
	
    #retrieve all the data from the table named "data"
    cur.execute("SELECT * FROM data")
    #return the set of all data
    rows = cur.fetchall()
    for row in rows:
        print row
	
    
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
