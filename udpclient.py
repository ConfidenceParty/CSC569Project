# udpclient.py

from socket import *
import time

SLEEP_TIME = 3
serverName = "unix4.csc.calpoly.edu"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:

   message = ""
   clientSocket.sendto(message.encode(), (serverName, serverPort))

   time.sleep(SLEEP_TIME)

# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print(modifiedMessage.decode())

clientSocket.close()
