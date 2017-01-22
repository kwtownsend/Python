# *******************************************************************
# This file illustrates how to send a file using an
# application-level protocol where the first 10 bytes
# of the message from client to server contain the file
# size and the rest contain the file data.
# *******************************************************************
import socket
import os
import sys


# Server address
serverAddr = "localhost"

# Server port
serverPort = 1234





# The number of bytes sent
numSent = 0

# The file data
fileData = None

ans=True
while ans ==True:
	print ("""
	1. get <file name> (downloads file <file name> from the server)
	2. put <filename> (uploads file <file name> to the server)
	3. ls (lists files on the server)
	4. quit (disconnects from the server and exits)
	""")
	ans=raw_input("What would you like to do? ") 
	if ans=="1": 
		# Create a TCP socket
		connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect to the server
		connSock.connect((serverAddr, serverPort))
		fileData=raw_input("Type in, get <file name> :") 

		if fileData:
			print "Client is downloading"
							
			# Get the size of the data read
			# and convert it to string
			dataSizeStr = str(len(fileData))
		
			# Prepend 0's to the size string
			# until the size is 10 bytes
			while len(dataSizeStr) < 10:
				dataSizeStr = "0" + dataSizeStr
		
		
			# Prepend the size of the data to the
			# file data.
			fileData = dataSizeStr + fileData	
			
			# The number of bytes sent
			numSent = 0
		
			# Send the data!
			while len(fileData) > numSent:
				numSent += connSock.send(fileData[numSent:])
			print "Client has Successfully downloaded"
			# The file has been read. We are done
			print "Sent ", numSent, " bytes."		
			connSock.close()
			ans = True
	elif ans=="2":
		# Create a TCP socket
		connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect to the server
		connSock.connect((serverAddr, serverPort))

		fileName=raw_input("Type in, put <file name> :")
		diddly = fileName.rsplit( ' ')
		fileName = diddly[1]
		# Open the file
		fileObj = open(fileName, "r")


		# The number of bytes sent
		numSent = 0

		# The file data
		fileData = None

		# Keep sending until all is sent
		# Read 65536 bytes of data
		fileData = fileObj.read(65536)
	
		# Make sure we did not hit EOF
		if fileData:
			
			
			# Get the size of the data read
			# and convert it to string
			dataSizeStr = str(len(fileData))
		
			# Prepend 0's to the size string
			# until the size is 10 bytes
			while len(dataSizeStr) < 10:
				dataSizeStr = "0" + dataSizeStr
		
	
			# Prepend the size of the data to the
			# file data.
			fileData = dataSizeStr + fileData	
			
			# The number of bytes sent
			numSent = 0
		
			# Send the data!
			while len(fileData) > numSent:
				numSent += connSock.send(fileData[numSent:])
		
		# The file has been read. We are done
		print "Sent ", numSent, " bytes."
		connSock.close()
		ans = True
	elif ans=="3":
		# Create a TCP socket
		connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect to the server
		connSock.connect((serverAddr, serverPort))
		fileData= "ls"
		if fileData:
							
			# Get the size of the data read
			# and convert it to string
			dataSizeStr = str(len(fileData))
		
			# Prepend 0's to the size string
			# until the size is 10 bytes
			while len(dataSizeStr) < 10:
				dataSizeStr = "0" + dataSizeStr
		
		
			# Prepend the size of the data to the
			# file data.
			fileData = dataSizeStr + fileData	
			
			# The number of bytes sent
			numSent = 0
		
			# Send the data!
			while len(fileData) > numSent:
				numSent += connSock.send(fileData[numSent:])
		
			# The file has been read. We are done
			print "Sent ", numSent, " bytes."		
			connSock.close()
			ans = True
	elif ans=="4":
		print("Goodbye")
		# Close the socket and the file
		connSock.close()
		fileObj.close()
		break 
	elif ans !="":
		print("\n Not Valid Choice Try again") 
		ans = True

