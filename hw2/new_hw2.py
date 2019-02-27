#!/usr/bin/env python3


from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup
import os

class people:
    def __init__(self, name, pa, dp, uid, phone = "0", title = "Nah"):
        self.name = name   #cn
        self.pa = pa       #osuPrimaryAffiliation
        self.title = title   #title
        self.dp = dp       #osuDepartment
        self.phone = phone   #telephoneNumber
        self.uid = uid     #uid
    def __repr__(self):
        str = ""
        str += "Name:\t" + self.name + "\n"
        if self.pa == "E" :
            str += "Primary Affiliation:\t" + "Employee" + "\n"
            str += "Title:\t" + self.title + "\n"
        elif self.pa == "S":
            str += "Primary Affiliation:\t" + "Student" + "\n"
        elif self.pa == "O":
            str += "Primary Affiliation:\t" + "Other" + "\n"
        if self.dp != "Nah":
            str += "Department:\t" + self.dp + "\n"
        if self.phone != "0":
            str += "Phone:\t" + self.phone.replace(" ","-") + "\n"
        str += "ONID Username:\t" + self.uid + "\n"
        return str

    def __str__(self):
        return self.__repr__();

def get_data():
    try:
        url_str = "http://directory.oregonstate.edu/?type=search&cn=" + sys.argv[1] +"+"+ sys.argv[2]
        print(url_str)
        url = urlopen(url_str)
        html = str(url.read())
        print(len(html))
        #print(html)
        soup = BeautifulSoup(html, 'html.parser')
        result = []
        for k in soup.find_all('div',class_='record'):
            print(k,"\n")
            result += k
        print(result[1])
        print(str(result[1]))
    except:
        print("Nah")
os.system("clear")
get_data()