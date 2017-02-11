#!/usr/bin/python
import psycopg2

try:
	conn = psycopg2.connect("dbname='myDB' user='postgres' host='10.0.0.8' password='anything123'")
	print "connection done!!!!!!!!!!!!"
except:
	print "connection fail"

cur = conn.cursor();
cur.execute("""select * from emp""");
rows = cur.fetchall();

for row in rows:
	print row;

