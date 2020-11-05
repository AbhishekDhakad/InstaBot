from time import sleep
from selenium import webdriver
import mysql.connector
import itertools
import follow

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",db="abhi")
mycursor = mydb.cursor()
#create table instabot(sr int auto_increment,following longtext,followers longtext,unfollower longtext, primary key(sr));

def info_list(driver,username):
	a=follow.info(driver,username,"following")
	b=follow.info(driver,username,"followers")
	c=[]
	print("Uploading data to database......")
	for i in a:
		if i not in b:
			c.append(i)
	j=[]
	for (x,y,z) in itertools.zip_longest(a,b,c):
		p=(x,y,z)
		j.append(p)
	query=("insert into instabot(following,followers,unfollower) values(%s,%s,%s)")
	mycursor.executemany(query,j)
	mydb.commit()
	print("Data uploaded Successfully")
	driver.quit()
	return 1



#create table info(sr int auto_increment,name varchar(30),username longtext,followers varchar(10),following varchar(10),posts varchar(10), primary key(sr))
def takeinfo(driver,victim,loc,choice):
	try:
		url='https://www.instagram.com/'+victim
		driver.get(url)
		txt1=driver.find_element_by_xpath('//*[@class="rhpdm"]').text
		txt2=driver.find_element_by_xpath('//a[contains(@href, "followers")]').text
		txt3=driver.find_element_by_xpath('//a[contains(@href, "following")]').text
		txt4=driver.find_element_by_xpath('//a[contains(@href, "posts")]').text
		Name=txt1
		username=victim
		followers =txt2.split()[0]
		following =txt3.split()[0]
		posts     =txt4.split()[0]
		a=(Name,username,followers,following,posts)
		path=loc+victim+"s.txt"
		file=open(r"%s"%(path,),"w")
		file.write("Name      ="+Name+"\n")
		file.write("username  ="+victim+"\n")
		file.write("followers =  %s"%followers+"\n")
		file.write("following =  %s"%following+"\n" )
		file.write("posts     =  %s"%posts+"\n")
		file.close()
		if(choice):
			query=("insert into info(Name,username,followers,following,posts) values(%s,%s,%s,%s,%s)")
			mycursor.execute(query,a)
			mydb.commit()
		print("Data uploaded Successfully")
		driver.quit()
		return 1
	except Exception as es:
		print(es)
		return 0