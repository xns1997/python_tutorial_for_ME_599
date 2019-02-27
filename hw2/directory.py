#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os
try:
    import ldap
except:
    os.system("pip install python-ldap")
    import ldap

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

def gen_people_obj():
    l = ldap.initialize('ldap://directory.oregonstate.edu:389')
    base = "o=orst.edu"
    name = make_name_query()
    result = l.search_s(base, ldap.SCOPE_SUBTREE, name)
    print (result)
    people_obj = []
    for i in range (len(result)):

        name = result[i][1]["cn"][0].decode("utf-8")
        pa = result[i][1]["osuPrimaryAffiliation"][0].decode("utf-8")
        try:
            dp = result[i][1]["osuDepartment"][0].decode("utf-8")
        except:
            dp = "Nah"
        uid = result[i][1]["uid"][0].decode("utf-8")
        try:
           phone = result[i][1]["telephoneNumber"][0].decode("utf-8")
        except:
           phone = "0"
        #print(result)
        try:
            title = result[i][1]["title"][0].decode("utf-8")
            temp = people(name,pa,dp,uid,phone,title)
        except:
            temp = people(name,pa,dp,uid,phone)
        people_obj += [temp]
    for i in range (len(people_obj)):
        print(people_obj[i])



def get_name():
    name = "";
    if(len(sys.argv) < 2):
        print ("nah")
    else:
        temp = sys.argv
        temp.pop(0)
        name += temp[1] + ", " +temp[0]
    return name

def make_name_query():
    name = "(cn=" + get_name() + ")"
    return name

os.system("clear")
"""
l = ldap.initialize('ldap://directory.oregonstate.edu:389')
base = "o=orst.edu"
name = "(cn=Parham-Mocello, Jennifer)"
name = make_name_query()
result = l.search_s(base, ldap.SCOPE_SUBTREE, name)
print("TYPE result 0:",type(result), (len(result)))
print(result[0][0])
print(result[0][1]["cn"])
print(type(result[0][1]["cn"][0]))
print("\n")
print(result)
"""
gen_people_obj()
