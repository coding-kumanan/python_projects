import os
import sys

cmd= "sudo yum install httpd -y"  
#&>>/tmp/log.txt"
if(os.system(cmd + '&>>/tmp/log.txt')) !=0:
    print ("Faililed to Execute the Cmd: " + cmd )
    exit (-1)
else:
    print ("HTTPD installed Successfully")
