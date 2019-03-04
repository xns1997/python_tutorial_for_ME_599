#!/usr/bin/env python3


from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup as BS
import os
from clear_console import clean_the_console
from tqdm import tqdm
import time
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
def make_query():
    if (len(sys.argv) - 1) % 2 != 0 :
        print("Wrong Name Length")
        return None
    elif len(sys.argv) == 1:
        print("No Name")
        return None
    else:
        query = []
        length = len(sys.argv)
        for i in range (int(length/2)):
            #print(2*i+1)
            #print(2*i+2)
            temp = sys.argv[2*i+1] + "+" + sys.argv[2*i+2]
            query += [temp]
        #print(query)   
        return query
def get_data_by_name(name):
        url_str = "http://directory.oregonstate.edu/?type=search&cn=" + name
        #print(url_str)
        '''
        url = urlopen(url_str)
        html = str(url.read())
        #print(len(html))
        #print(html)
        soup = BS(html, 'html.parser')
        '''
        soup = cook_soup(url_str)
        result = []
        datas = soup.find_all('div',class_='record')
        #print('len: ',len(datas))
        if len(datas) == 1:
            tag = datas[0].find_all('b')
            data = datas[0].find_all('dd')
            result = [data_con(tag,data)]
            #print('Result:') 
            #print(result[0])
            return result
        elif len(datas) > 1:
            temp = name.split('+')
            links = soup.find_all('a', href=True,text=temp[1] +", "+ temp[0])
            #print(links[0]['href'])
            for i in links:
                url_str = "http://directory.oregonstate.edu" + i['href']
                #print(url_str)
                '''
                url = urlopen(url_str)
                html = str(url.read())
                each_soup = BS(html, 'html.parser')
                '''
                each_soup = cook_soup(url_str)
                datas = each_soup.find_all('div',class_='record')
                tag = datas[0].find_all('b')
                data = datas[0].find_all('dd')
                result += [data_con(tag,data)]
            #print('Results:')
            return result
        else:
            print('No This Guy')
            return None
def search():
    query = make_query()
    pbar = tqdm(query)
    try:
        for name in pbar:
            pbar.update()
            result = get_data_by_name(name) 
            for data in result:
                print(data)
            
            
    except:
        print("Invalid Input")

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

def cook_soup(url_str):
    try:
        url = urlopen(url_str)
        html = str(url.read())
        soup = BS(html, 'html.parser')
        return soup
    except:
        print('No this website')
        return None
    


def count_tt(title):
    url = urlopen('https://mime.oregonstate.edu/people')
    html = str(url.read())
    soup = BS(html, 'html.parser')
    datas = soup.find_all(lambda tag:tag.name=="p" and title in tag.text )
    print(title,": ",len(datas))

clean_the_console( )
search()
count_tt("Assistant Professor")
count_tt("Associate Professor")
#count_title('Assistant Professor','Sch of Mech/Ind/Mfg Engr')
#count_title('Associate Professor','Sch of Mech/Ind/Mfg Engr')
