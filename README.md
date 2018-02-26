# CSC569Project

Heartbeat Scripts

udpclient.py
- Assumes server name is "unix4.csc.calpoly.edu"
- Sends a message containing an empty string to the server and then sleeps for SLEEP_TIME seconds

udpserver.py
- Listens for messages using a non-blocking socket (timeout threshold of THRESHOLD seconds)
- Receives message from worker and updates the workerList dict (key: worker IP address, value: message timestamp)
- Every THRESHOLD seconds, checks whether a heartbeat has been received from each worker within THRESHOLD seconds
- Outputs message to stdout when heartbeat received from a worker
- Outputs message to stdout when worker is down (i.e. heartbeat not received within THRESHOLD)
