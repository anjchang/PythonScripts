#!/usr/bin/python
# -*- coding: utf-8 -*-
#count occurence of device data in a csv file
import csv
import sys

my_reader = csv.reader(open('out.csv'))
whictr = 0
bluctr=0
redctr=0
yelctr = 0
broctr =0
oractr = 0
purctr = 0
grectr =0

for record in my_reader:
	if 'TinkrWord' in record[3]:
		if 'white' in record[3]:
			whictr += 1
		if 'blue' in record[3]:
			bluctr += 1
		if 'red' in record[3]:
			redctr += 1
		if 'yellow' in record[3]:
			yelctr += 1
		if 'brown' in record[3]:
			broctr += 1
		if 'orange' in record[3]:
			oractr += 1
		if 'purple' in record[3]:
			purctr += 1
		if 'green' in record[3]:
			grectr += 1
	
print 'number of white entries: %s' %whictr
print 'number of blue entries: %s' %bluctr
print 'number of red entries: %s' %redctr
print 'number of yellow entries: %s' %yelctr
print 'number of brown entries: %s' %broctr
print 'number of orange entries: %s' %oractr
print 'number of purple entries: %s' %purctr
print 'number of green entries: %s' %grectr

