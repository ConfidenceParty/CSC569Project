# udpserver.py

from socket import *
import time

HEARTBEAT_COUNT = 10
THRESHOLD = 5

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
serverSocket.settimeout(THRESHOLD)

workerList = {}
lastTime = time.time()

print("The server is ready to receive")

while True:
   try:
      message, clientAddress = serverSocket.recvfrom(2048)
      print("Heartbeat from {}".format(clientAddress))
      workerList[clientAddress[0]] = time.time()
   except timeout:
      print("No heartbeats received in {} seconds".format(THRESHOLD))
      workerList.clear()

   if (time.time() - lastTime) > THRESHOLD and len(workerList) > 0:
      curTime = time.time()
      for key in workerList:
         if (curTime - workerList[key]) > THRESHOLD:
            print(key, end=" ")
            print("is down")
      lastTime = time.time()

   # Change client message to all uppercase
   #modifiedMessage = message.decode().upper()
   
   #serverSocket.sendto(modifiedMessage.encode(), clientAddress)

