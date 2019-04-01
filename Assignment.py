import requests
import mysql.connector
from mysql.connector import Error
from bs4 import BeautifulSoup
from Exception import DataException


def mysql_decorator(func):
    def inner(x):
        try:
            mySQLconnection = mysql.connector.connect(host='localhost',
                                                      database='PYTHON_assignment',
                                                      user='admin',
                                                      password='')
            sql_select_Query = "select * from users"
            cursor = mySQLconnection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            check = False
            for row in records:
                if x == row[0]:
                   check = True
            if check:
                print(f'Yes {x} exist')
                returned_value = func(x)
        
            else:
                raise Exception('Sorry user don\'t exist')
            cursor.close()
            return returned_value
        
        except Error as e:
            print("Error while connecting to MySQL", e)
    return inner

@mysql_decorator
def scrap(name):
    URL = f"https://en-gb.facebook.com/{name}"
    for person in person_scrapped:
        if person.username == name:
            return person.show_values()
    try:
        r = requests.get(URL)
    except:
        print("User does not exist in facebook")
    
    soup = BeautifulSoup(r.content, 'html5lib')
    Name = soup.find(attrs={'class':'_2nlw _2nlv'}).contents[0]
    City = soup.find(attrs={'class':'_2iel _50f7'}).find('a').contents[0]
    Work = []
    try:
        for tags in soup.find(attrs={'class':'_4qm1'}).findAll(attrs={'class': '_2lzr _50f5 _50f7'}):
            Work.append(tags.find('a').contents[0])
    except:
        print("Work does not exist")
    categories = {}
    try:
        for rows in soup.find(attrs={'class': 'mtm _5e7- profileInfoTable _3stp _3stn'}).findAll('tbody'):
            if rows.find(attrs={'class': 'labelContainer'}).contents[0] != 'Other':
                categories.update({rows.find(attrs={'class':'labelContainer'}).contents[0]: rows.find(attrs={'class':'mediaPageName'}).contents[0]})
    except:
        pass
    
    if len(categories) == 0:
        print('Favourites does not exist')
    else:
        print(categories)
    person = Person(name, Name, City, Work)
    person_scrapped.append(person)
    return "Drumil"
    
    

class Person:
    """
    hioj
    """
    def __init__(self, username=None, name=None, work=[], city='Roorkee'):
        if username != None:
            self.username = username
        self.name = name
        if work != []:
            self.work = work
        self.city = city
    
    def show_values(self):
        self.message =  f"My name is {self.name} and my current city is {self.work}"
        print(self.message)
        return self.message

global person_scrapped
person_scrapped = []

if __name__ == '__main__':
    while True:
        x = input("Find users ")
        scrap(x)