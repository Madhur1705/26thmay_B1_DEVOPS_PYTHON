import time
import psutil
import os
from getmac import get_mac_address as mac;

user_input='''
Press 1 to Check current time and Date :- 
Press 2 to Check RAM Size of Your current OS  :- 
Press 3 to KNow Name of YOur current OS :- 
Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
Press 5 to create one directory IN your Desktop :- 
'''
print(user_input)
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
    print("Invalid Key")    
