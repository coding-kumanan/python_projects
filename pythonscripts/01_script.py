import os
import sys

cmd = ["sudo yum install httpd -y", "sudo systemctl enable httpd", "sudo systemctl restart httpd "]  
for i in cmd:
    if(os.system(i + '&>>/tmp/log.txt')) !=0:
        print ("Faililed to Execute the Cmd: " + cmd )
        exit (-1)
print("HTTP configured Successfully")
