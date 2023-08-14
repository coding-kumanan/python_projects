import os
import sys
def mes(status , i):
    if (status !=0):
        print(i +  ":failed")
        exit(-1)
    else:
         print(i + ":success")
          

cmd = ["sudo yum install nginx -y", "sudo systemctl enable nginx", "sudo systemctl start nginx "] 
print("Installing Nginx")
for i in cmd:
    status=(os.system(i + '&>>/tmp/log.txt'))
    mes(status, i)

print("Downloading HTML Files")
i='curl -s -L -o /tmp/frontend.zip "https://github.com/stans-robot-project/frontend/archive/main.zip"'
status=(os.system(i)
mes(status, i)        
        