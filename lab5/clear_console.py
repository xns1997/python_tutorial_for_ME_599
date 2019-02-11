import sys
import os
import platform

def clean_the_console( ):
    sysstr = platform.system()
    if(sysstr =="Windows"):  #Windows NT only
        clear = lambda : os.system('cls') 
        clear()
    elif(sysstr == "Linux"):  #Ubuntu,Deepin,CentOS......
        clear = lambda : os.system('clear') 
        clear()
    elif(sysstr == "Darwin"):  #MacOS
        clear = lambda : os.system('clear') 
        clear()
    else:
        print ("Other System tasks")