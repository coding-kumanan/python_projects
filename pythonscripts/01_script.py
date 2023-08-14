import os
import sys
def mes(status , i):
    if (status !=0):
        print(i +  ":failed")
        exit(-1)
    else:
         print(i + ":success")
          
cmd = ["sudo yum install httpd -y", "sudo systemctl enable httpd", "sudo sytemctl restart httpd "] 

for i in cmd:
    status=(os.system(i + '&>>/tmp/log.txt'))
    mes(status, i)