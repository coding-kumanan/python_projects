import os
import sys

cmd= "sudo yum install httpd -y"
cmd1 = "/tmp/logfile.txt"
os.system(cmd)
id=os.system("$?") 
if(id != 0):
    print ("Faililed to Execute the Cmd" + cmd )
    exit (-1)