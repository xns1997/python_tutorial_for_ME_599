#!/usr/bin/env python3


from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup
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
        str += " +---------------------+-----------------------------------+\n"
        str += "  Name:\t\t\t" + self.name + "\n"
        if self.pa == "Employee" :
            str += "  Primary Affiliation:\t" + "Employee" + "\n"
            str += "  Title:\t\t" + self.title + "\n"
        elif self.pa == "Student":
            str += "  Primary Affiliation:\t" + "Student" + "\n"
        elif self.pa == "Other":
            str += "  Primary Affiliation:\t" + "Other" + "\n"
        if self.dp != "Nah":
            str += "  Department:\t\t" + self.dp + "\n"
        if self.phone != "0":
            str += "  Phone:\t\t" + self.phone.replace(" ","-") + "\n"
        str += "  ONID Username:\t" + self.uid + "\n"
        str += " +---------------------+-----------------------------------+\n"
        return str

    def __str__(self):
        return self.__repr__();

def get_data_by_name():
        url_str = "http://directory.oregonstate.edu/?type=search&cn=" + sys.argv[1] +"+"+ sys.argv[2]
        #print(url_str)
        url = urlopen(url_str)
        html = str(url.read())
        #print(len(html))
        #print(html)
        soup = BeautifulSoup(html, 'html.parser')
        result = []
        datas = soup.find_all('div',class_='record')
        #print('len: ',len(datas))
        if len(datas) == 1:
            tag = datas[0].find_all('b')
            data = datas[0].find_all('dd')
            result = [data_con(tag,data)]
            print('Result:') 
            print(result[0])
        elif len(datas) > 1:
            links = soup.find_all('a', href=True,text=sys.argv[2] +", "+ sys.argv[1])
            #print(links[0]['href'])
            for i in links:
                url_str = "http://directory.oregonstate.edu" + i['href']
                #print(url_str)
                url = urlopen(url_str)
                html = str(url.read())
                each_soup = BeautifulSoup(html, 'html.parser')
                datas = each_soup.find_all('div',class_='record')
                tag = datas[0].find_all('b')
                data = datas[0].find_all('dd')
                result += [data_con(tag,data)]
            print('Results:')
            for i in result:
                print(i)
        else:
            print('Nah')
  

def data_con(tag,data):
    name= ''
    pa = ''
    dp = 'Nah'
    tt = 'Nah'
    phone = '0'
    uid = ''
    for i in range (len(tag)):
        if tag[i].text == 'Full Name':
            name = data[i].text
            #print(name)
        elif tag[i].text == 'Primary Affiliation':
            pa = data[i].text
            #print(pa)
        elif tag[i].text == 'Department':
            dp = data[i].text
            #print(dp)
        elif tag[i].text == 'ONID Username':
            uid = data[i].text
            #print(uid)
        elif tag[i].text == 'Office Phone Number':
            phone = data[i].text
            #print(phone)
        elif tag[i].text == 'Title':
            tt = data[i].text
            #print(tt)

    return people(name,pa,dp,uid,phone,tt)

def make_query(title,dp):
    name = "(&(title=" + title + ")(osuDepartment="+dp+"))"
    print(name)
    return name

def count_title(title,dp):
    l = ldap.initialize('ldap://directory.oregonstate.edu:389')
    base = "o=orst.edu"
    query = make_query(title,dp)
    #query =[title,dp]
    result = l.search_s(base, ldap.SCOPE_SUBTREE, query)
    #print (result)
    print (title,": ",len(result))
    

os.system("clear")
get_data_by_name()
count_title('Assistant Professor','Sch of Mech/Ind/Mfg Engr')
count_title('Associate Professor','Sch of Mech/Ind/Mfg Engr')