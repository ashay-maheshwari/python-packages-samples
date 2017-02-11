#Ashay Maheshwari, MArch 8, 2016
#Module to connect to Mysql database using MySQLdb package 

import MySQLdb as mdb 

def connect_db(host, username, password, db_name):
        """
                Purpose         :       Function to connect to database using MySQLdb package.
                Input Values    :       Mysql Server IP/host name, username ,password and database name to connect
                Output Values   :       Returns a list of connection object if success
                                        Returns "Fail" if connection is not established"
        """

        try:
                print "Connecting to database"
                db_con = mdb.connect(host, username, password, db_name)
                cursor = db_con.cursor()
                print "Connection established"

		sql_query = """CREATE TABLE IF NOT EXISTS mails	(
				TO_ID VARCHAR(30),
				FROM_ID VARCHAR(30),
				DATE_ID VARCHAR(30),
				SUBJECT VARCHAR(500),
				CONTENT TEXT.
				CONSTRAINT primary_k PRIMARY KEY (DATE_ID));"""
                cursor.execute(sql_query)
		db_con.commit()

                return [db_con, cursor] 

        except:
                return "fail"     



def insert(data_list, con_object, cursor):
	"""
		Purpose		:	Function to insert data into Mysql database
		Input values	:	List containing the data, connection object for database and cursor object 
		Output values	:	Returns "success" if data gets inserted, else "fail"
	"""			

	if len(data_list) == 0:
		return "fail"
	else:
		for mail in data_list:
			try:
				insert_query = """INSERT INTO mails (TO_ID, FROM_ID, DATE_ID,SUBJECT,CONTENT) VALUES ('%s', '%s', '%s', '%s','%s')""" % (mail[0], mail[1], mail[2], str(mdb.escape_string(mail[3])), str(mdb.escape_string(mail[4])))
				cursor.execute(insert_query)
				con_object.commit()
				
			except:
				return "fail"
		return "success"

def fetch_data(con_object, cursor):
        """
                Purpose         :       Function to fetch data from database
                Input values    :       Connection object and cursor object
                Output values   :       Returns data list fetched or "fail"
        """
        try:
                sql_query = """SELECT * from mails"""
                cursor.execute(sql_query)
                data = cursor.fetchall()
                return data 
        else:
                return "fail"
