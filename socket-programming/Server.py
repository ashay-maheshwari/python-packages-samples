#!/usr/bin/python

import logging 
import socket
import  sys

####################################################################

logger = logging.getLogger("Running Server")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

ch.setFormatter(formatter)
logger.addHandler(ch)

####################################################################
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
server_address = ('localhost', 20003)

sock.bind(server_address)
#print "Starting up in %s port %s " % sock.getsockname()
logger.info("STarting up")


sock.listen(1)


while True:
	#print "waiting for a connection"
	logger.info("waiting for a connection")
	try:
		connection, client_addr = sock.accept()
		#print "client conencted", client_addr
		logger.info("client conencted")
		data  = connection.recv(4096)
		#print "Received -- ", data
		logger.info("Received -- ")
		if data == """CONNECTION^`!XML^`!SOMESTRING#END#""":
			ack_str = """CONNECTION!0"""
			connection.send(ack_str)
			#print "Sending back the ACK String"
			logger.info("Sending back the ACK String")
			new_data = connection.recv(4096)
			#print "Receiving message sent from client"
			logger.info("Receiving message sent from client")
			print new_data
			if new_data:
				msg_status_str = """ACK!MSGSTATUS=TRUE"""
				connection.send(msg_status_str)
				#print "Message ACK sent to Client.MESSAGE SEND"
				logger.info("Message ACK sent to Client.MESSAGE SEND")
			else:
				msg_status_str = """ACK!MSGSTATUS=FALSE"""
				connection.send(msg_status_str)
				#print "Message ACK sent to Client. CANNOT SEND"
				logger.info("Message ACK sent to Client. CANNOT SEND")

			close_str_recvd = connection.recv(4096)
			print "######",close_str_recvd
			
			if close_str_recvd:
				#print "Received close conenction string from client"
				logger.info("Received close conenction string from client")
				#print "Server said -- Good bye"
				logger.info("Server said -- Good bye")
			break
		else:
			break
	
	except:
		print "this is outer  expect"	
	finally:
		#print "Server closing connection" 
		logger.info("Server closing connection")
		sock.close()





