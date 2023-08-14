import os
import sys

cmd= "sudo yum install httpd -y"
if os.system('cmd' '> log.txt') !=0: 
    print ("Faililed to Execute the Cmd" + cmd )
    exit (-1)