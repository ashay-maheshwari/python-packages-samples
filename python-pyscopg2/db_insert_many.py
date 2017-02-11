#!/usr/bin/python

import psycopg2


try:
 con=psycopg2.connect("dbname='myDB' user='postgres' host='10.0.0.8' password='anything123'");
 print "Connection successful";
except:
 print "No connection";


cur=con.cursor();
lst=[['Ashay','Ashta'],['Mayur','Bhopal']];
tup=tuple(lst);

try:
 q="INSERT INTO three values(%s,%s,'default');";
 cur.executemany(q,tup);
 con.commit();
except:
 print "Cant insert";
