# 26thmay_B1_DEVOPS_PYTHON
Tasksimport time
import psutil
import os
from getmac import get_mac_address as mac;
y = eval(input("Press the key: "))
print(y)
if y==1 :
    z = time.ctime()
    print("The current is : ", z)

elif y==2 :
    m = psutil.virtual_memory().total
    print("RAM Size of current OS is ",(m/(1024**3)),"GB")

elif y==3 :
    print("name of the current OS: ",os.uname())

elif y==4 :
    print("MAC Address ", mac())
elif y==5 :
    path = "/home/madhur/Desktop/created"
    print("Create a new directory in desktop",os.mkdir(path,754))
else :
    print("wrong")
