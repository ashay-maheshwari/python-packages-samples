#!/usr/bin/python
#Ashay Maheshwari, March 2016
#Python script to read emails from gmail account using IMAP-python module 

import sys
import imaplib
import email
import MySQLdb as mdb



needed_list = []
all_mail_list = []

def connect_and_retrieve1(mail_id, password, folder):
	"""
	   Function is responsible for connecting to email account using IMAP protocol
           and based on the folder selected for retrieving mail from, will pick out 
           To, From, body, Subject and date of the mail sent
        """

	try:
		mail = imaplib.IMAP4_SSL('imap.gmail.com')
		mail.login(mail_id, password)
		mail.select(folder)

		result, data = mail.search(None, 'ALL')

		ids = data[0]
		id_list = ids.split()
	except:
		return "fail"


	for email_id in id_list:
       		needed_list = []
		result, data = mail.fetch(email_id, "(RFC822)")
		raw_email = data[0][1]
	
		email_message = email.message_from_string(raw_email)
		email_to = email_message['To']
		email_from = email.utils.parseaddr(email_message['From'])
	
		needed_list.append(email_to)
		needed_list.append(email_from[1])
	
		header_list = email_message.items()
	
		for item in header_list:
			if 'Subject' in item:
				needed_list.append(item[1])
			if "Date" in item:
				needed_list.append(item[1])

		for part in email_message.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True)
				needed_list.append(body)

		all_mail_list.append(needed_list)
		data_list = all_mail_list

	#return data_list
	return all_mail_list

	
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
		Purpose		:	Function to fetch data from database
		Input values	:	Connection object and cursor object
		Output values	:	Returns data list fetched or "fail"
	"""

	sql_query = """SELECT TO, FROM, DATE, CONTENT FROM mail_table"""
	cursor.execute(sql_query)
	data = cursor.fetchone()
	print data



email_status = connect_and_retrieve1("some.user@gmail.com", "somepassword", "inbox")
if "fail" == email_status:
	print "Mail was not fetched. Exiting..."
	exit(1)
	
else:
	connection_status = connect_db("localhost", "user_name", "somepassword", "mydb")
	

if "fail" == connection_status:
	print "Database connection issues. Please check again"
	exit(1)
else:
	insert_status = insert(email_status, connection_status[0], connection_status[1])
	if "fail" in insert_status:
		print "Data was not inserted"
	else:
		print "Data was inserted successfully"



