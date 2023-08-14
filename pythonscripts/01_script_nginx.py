import os
import sys
def mes(status , i):
    if (status !=0):
        print(i +  ":failed")
        exit(-1)
    else:
         print(i + ":success")
          
cmd = ["sudo yum install nginx -y", "sudo systemctl enable nginx", "sudo systemctl start nginx "] 

for i in cmd:
    status=(os.system(i + '&>>/tmp/log.txt'))
    mes(status, i)