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

print("---------------\nDownloading HTML Files")
i='curl -s -L -o /tmp/frontend.zip "https://github.com/stans-robot-project/frontend/archive/main.zip"'
status=(os.system(i))
mes(status, i)  
print("---------------\nDeploy in Nginx Default Location")
cmd = ["cd /usr/share/nginx/html","rm -rf *","unzip -o /tmp/frontend.zip","mv frontend-main/* .","mv static/* .","rm -rf frontend-main README.md","mv localhost.conf /etc/nginx/default.d/roboshop.conf"]    
for i in cmd:
    status=(os.system(i + '&>>/tmp/log.txt'))
    mes(status, i)     