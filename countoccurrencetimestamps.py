#!/usr/bin/python
# -*- coding: utf-8 -*-
#count occurence of device data in a csv file
import csv
import sys

my_reader = csv.reader(open('week6.csv'))
ctr = 0
for record in my_reader:
	if record[1] == 'device':
		ctr += 1
	
print 'number of timestamp entries: %s' %ctr
