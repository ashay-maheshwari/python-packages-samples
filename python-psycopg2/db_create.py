#!/usr/bin/python

import psycopg2

try:
	conn = psycopg2.connect("dbname='myDB' user='postgres' host='10.0.0.23' password='anything123'")
	print "connection done.........."
except:
	print "connection fail"
cur = conn.cursor();
try:
	cur.execute("""create table emp1(name varchar(20), addr varchar(20), sal int);""");
	print "table is created"
	conn.commit();
except:
	print "creation fail"

