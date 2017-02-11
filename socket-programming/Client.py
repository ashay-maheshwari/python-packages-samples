#!/usr/bin/python

#######################################################################
#IMPORT STATEMENTS
######################################################################
import logging
import time
import  socket
import sys
import errno 

######################################################################
#CODE FOR ENABLING LOGGING
#######################################################################

logger = logging.getLogger("Running Client")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

ch.setFormatter(formatter)
logger.addHandler(ch)





#####################################################################
#XML MESSAGE FORMAT TO BE SENT TO AND FROM SMS GATEWAY
#####################################################################

xml_format_msg = """
        <MOBILE>8484900438</MOBILE>
        <MESSAGE>Sample message. This is testing.</MESSAGE>
"""

#############################################################################
#MESSAGE FORMED AS PER THE STANDARD MENTIONED IN THE DOUCMENT 
############################################################################
send_message = """MESSAGE^'!""" + xml_format_msg + """#END#"""


#############################################################################
#CREATING A SOCKET OBJECT 
############################################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#SERVER ADDRESS TO CONNECTIONENCT TO 
server_address = ('localhost', 20003)
#print "Connecting to server  %s at port %s " % server_address
logger.info("Connecting to server")

#############################################################################
#ESTABLISHING A SCOKET CONNECTIONNECTION
###########################################################################
try:
	sock.connect(server_address)
except socket.error as serr:
	if serr.errno == errno.ECONNECTIONNREFUSED:
		#print "CONNECTIONNECTION NOT AVAILABLE"
		logger.error("Connection not availaable")
	else:
		raise
	
	
#############################################################################
#TRYING TO ESTABLISH A SEQUENTIAL CONNECTIONNECTION WITH SERVER
#############################################################################
try:
	#CONNECTIONNECTION STRING TO BE SENT TO SERVER TO INIATIALIZE THE MESSAGE CONNECTIONNECTION 
	init_str = """CONNECTION^`!XML^`!SOMESTRING#END#"""
	
	#print "Sedning -- " , init_str
	logger.info("Sending ---")
	sock.sendall(init_str)
	#print "SENDING INITIALIZATION STRING %s TO SMS GATEWAY SERVER" % init_str
	logger.info("Sending initialization string to send to sms gateway")
	
	amt_recvd =  0
	amt_expected = len(init_str)
	
	data = sock.recv(26)
	#print "WAITING FOR  ACKNOWLEDGE STRING %s FROM SERVER -- CONNECTION!0" 
	logger.info("Waiting for ack ")
	if data == """CONNECTION!0""":
		#print "RECIVED ACKNOWLEDGE STRING FROM SERVER"
		logger.info("Received ack string from server")
		#print "Client is closing the conenction"
		#sock.close()
		#print "WILL SEND MESSAGE TO SERVER"
		logger.info("Will send message to service")
		sock.sendall(send_message)
		#print "MESSAGE SENT TO SERVER"
		logger.info("Message sent to server")
		#print "WAITING FOR SERVER RESPONSE"
		logger.info("Message sent to server")

		#time.sleep(100)
		msg_ack_str = sock.recv(4096)
		#print "RECEIVED SERVER RESPONSE FOR MESSAGE STATUS"
		logger.info("RECEIVED SERVER RESPONSE FOR MESSAGE STATUS")

		msg_status_true = """ACK!MESSAGESTATUS=TRUE"""
		msg_status_false = """ACK!MESSAGESTATUS=FALSE"""

		if msg_ack_str == msg_status_true:
			#print "SERVER SAID -- MESSAGE IS SENT"
			logger.info("SERVER SAID -- MESSAGE IS SENT")
			#print "NOW CLOSING MESSAGE SERVER CONNECTIONNECTION"
			logger.info("NOW CLOSING MESSAGE SERVER CONNECTIONNECTION")
			msg_end_str = """EXT^`!CLOSE the Message#END#"""
			sock.sendall(msg_end_str)
			#print "CLOSE MESSAGE CONNECTIONNECTION STRING SENT TO SERVER"
			logger.info("CLOSE MESSAGE CONNECTIONNECTION STRING SENT TO SERVER")
			#print "WAITING FOR SERVER RESPONSE"
			logger.info("WAITING FOR SERVER RESPONSE")

		if msg_ack_str == msg_status_false:
				#print "SERVER FAILED TO SEND MESSAGE.PLEASE  TRY AGAIN"	
				logger.info("SERVER FAILED TO SEND MESSAGE.PLEASE  TRY AGAIN")
						
		close_msg_str = """EXT^`!CLOSE the Message#END#"""
		sock.sendall(close_msg_str)
		#print "NO MORE MESSAGE TO BE SENT. CLIENT IS CLOSING CONNECTIONNECTION"
		logger.info("NO MORE MESSAGE TO BE SENT. CLIENT IS CLOSING CONNECTIONNECTION")
		#print "CLIENT SAID GOODBYE"
		logger.info("CLIENT SAID GOODBYE")
		#print "CLOSING CONNECTIONNECTION FROM CLIENT SIDE"
		logger.info("CLOSING CONNECTIONNECTION FROM CLIENT SIDE")
		sock.close()

except socket.error as e:
	if e.errno == errno.ECONNECTIONNREFUSED:
		print "CONNECTIONNECTION IS REFUSED DUE TO CERTAIN PROBLEM"
	else:
		raise 
	
finally:
	#print "CLIENT CLOSED CONNECTIONENCTION"
	logger.info("CLIENT CLOSED CONNECTIONENCTION")
	sock.close()
	
			


