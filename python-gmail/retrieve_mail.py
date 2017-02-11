#!/usr/bin/python
#Ashay Maheshwari, March 2016
#Python script to read emails from gmail account using IMAP-python module 


import sys
import imaplib
import email


def connect_and_retrieve(mail_id, password, folder):
	"""
	   Function is responsible for connecting to email account using IMAP protocol
           and based on the folder selected for retrieving mail from, will pick out 
           To, From, body, Subject and date of the mail sent
        """
	needed_list = []
	all_mail_list = []

 
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(mail_id, password)
	mail.select(folder)

	result, data = mail.search(None, 'ALL')

	ids = data[0]
	id_list = ids.split()


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

		for part in email_message.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True)
				needed_list.append(body)

		all_mail_list.append(needed_list)

	for mail in all_mail_list:
		#if mail[1] == "ashay@vlabs.ac.in":
			for section in mail:
				print section
			print "----------------------------------------------------------------------------------------------------------------------------"


