from time import sleep
from selenium import webdriver


def takeinfo(driver,usr):
	try:
		url='https://www.instagram.com/'+ usr
		driver.get(url)
		txt1=driver.find_element_by_xpath('//*[@class="rhpdm"]').text
		try:
			txt2=driver.find_element_by_xpath('//a[contains(@href, "followers")]').text    #public
		except:
			txt2 = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/span/span').text #private
		try:
			txt3=driver.find_element_by_xpath('//a[contains(@href, "following")]').text
		except:
			txt3=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/span/span').text

		txt4=driver.find_element_by_xpath('//*[@class="g47SY "]').text
		Name=txt1
		followers =txt2.split()[0]
		following =txt3.split()[0]
		posts     =txt4.split()[0]
		path="\\instabot\\"+usr+"_info.txt"
		file=open(r"%s"%(path,),"w")
		file.write("Name      ="+Name+"\n")
		file.write("username  ="+usr+"\n")
		file.write("followers =  %s"%followers+"\n")
		file.write("following =  %s"%following+"\n" )
		file.write("posts     =  %s"%posts+"\n")
		file.close()
		return [Name,followers,following,posts]
	except Exception as es:
		print(es)
		return 0