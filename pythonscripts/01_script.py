import os
import sys

cmd= "sudo yum install httpd -y &>>/tmp/log.txt"
if(os.system(cmd)) !=0:
    print ("Faililed to Execute the Cmd" + cmd )
    exit (-1)