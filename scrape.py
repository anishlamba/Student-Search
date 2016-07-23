import re
import json
from bs4 import BeautifulSoup
from urllib2 import *
import MySQLdb
import MySQLdb

#Connecting to Database 
connection = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="ssdb")
x = connection.cursor()



print ("Enter Roll Number:")
j =int(input())

# URL for Roll number detail
url=("http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes.jsp?typ=stud&numtxt=%d&sbm=Y" %j)
#Intially setting all variables to "NULL"
NAME=DEPARTMENT=BRANCH=IITK_ADDRESS=IITK_EMAIL=BLOOD_GROUP=CATEGORY=GENDER=COUNTRY=FATHER_NAME=PERMANENT_ADDRESS=CONTACT1=CONTACT2="NULL"
ROLL_NUMBER=-1
#Requesting to read Page and Converting it to Soup
page=urlopen(url)
soup = BeautifulSoup(page.read())
#check will be None for a valid Roll number request
check=soup.find("div",{"class":"DivAlertMessage"})
if check is None :
	# Converting Comments to a HTML so that we can scrape comments to
	p = re.compile( '(<!--|--!>|Phone no:|Mobile no:)')
	#Reconverting to Soup Object
	soup=p.sub( ' ', str(soup))
	soup = BeautifulSoup(soup)
	# Actual Scrapping Starts 8|
	temp=soup.find("td", { "class" : "TableContent" })
	temp1=list(temp.descendants)
	#Saving the Information in variables
	ROLL_NUMBER=int(temp1[3].strip())
	NAME=temp1[12].strip()
	DEPARTMENT=temp1[18].strip()
	BRANCH=temp1[24].strip()
	IITK_ADDRESS=temp1[30].strip()
	IITK_EMAIL=temp1[39].strip()
	BLOOD_GROUP=temp1[46].strip()
	CATEGORY=temp1[49].strip()
	GENDER=temp1[56].strip()
	COUNTRY=temp1[59].strip()
	FATHER_NAME=temp1[77].strip()
	PERMANENT_ADDRESS=temp1[79].strip()
	CONTACT1=temp1[81].strip()
	CONTACT2=temp1[83].strip()

# Scraping Part is Done Now we have to Save it

# Data Insert into the table
print("-------------------------------------------")
# length=len(temp1)
# for item in xrange(0,length):
# 	print(str(item))
# 	print(" - ")
# 	print(temp1[item])
# 	print("\n")
print("ROLL_NUMBER:%d"%ROLL_NUMBER)
print("NAME:%s"%NAME)
print("DEPARTMENT:%s"%DEPARTMENT)
print("BRANCH:%s"%BRANCH)
print("IITK_ADDRESS:%s"%IITK_ADDRESS)
print("IITK_EMAIL:%s"%IITK_EMAIL)
print("BLOOD_GROUP:%s"%BLOOD_GROUP)
print("CATEGORY:%s"%CATEGORY)
print("GENDER:%s"%GENDER)
print("COUNTRY:%s"%COUNTRY)
print("FATHER_NAME:%s"%FATHER_NAME)
print("PERMANENT_ADDRESS:%s"%PERMANENT_ADDRESS)
print("CONTACT1:%s"%CONTACT1)
print("CONTACT2:%s"%CONTACT2)



# x.execute("""INSERT INTO `details` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(ROLL_NUMBER,NAME,DEPARTMENT,BRANCH,IITK_ADDRESS,IITK_EMAIL,BLOOD_GROUP,CATEGORY,GENDER,COUNTRY,PERMANENT_ADDRESS,CONTACT1,CONTACT2,'NO'))
# connection.commit()

# connection.close()
## End of Code ! 