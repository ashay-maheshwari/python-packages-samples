#!/usr/bin/python

import psycopg2

try:
	conn =psycopg2.connect("dbname='myDB' user='postgres' host='10.0.0.23' password='anything123'")
	print "connection done"
except:
	print "connection fail"

try:
	cur = conn.cursor()
	cur.execute("""insert into emp1 values('mayur','khm',2000)""")
	print "data is inserted"
	conn.commit()
except:
	print "data is not inserted"

