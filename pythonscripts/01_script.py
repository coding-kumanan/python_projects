import os
import sys

cmd= "sudo yum install httpd -y"
os.system(cmd >> /tmp/log.txt)
id=os.system("$?") 
if(id != 0):
    print ("Faililed to Execute the Cmd" + cmd )
    exit (-1)