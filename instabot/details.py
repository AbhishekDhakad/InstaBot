from selenium import webdriver
from time import sleep
import urllib.request
import os

def savebio(driver,usr):
	try:
		url='https://www.instagram.com/'+usr
		driver.get(url)
		txt=driver.find_element_by_xpath('//*[@class="-vDIg"]').text
		try:
			os.mkdir('Bio')
		except:
			pass
		cur = os.getcwd()
		path = cur + "\\bio\\"  + usr + ".txt"
		bio=""
		for e in txt:
			if(ord(e)<=128):
				bio=bio+e
			else:
				bio=bio+"*"
		file=open(r"%s"%(path,),"w")
		file.write(bio)
		file.close()
		print("_____Bio saved SUCCESSFULLY_____")
		print("At location --->>>"+path)
		return 1
	except Exception as es:
		print(es)
		return 0

def dpdownload(driver,usr):
	try:
		url='https://www.instagram.com/'+usr
		driver.get(url)
		try:
			image=driver.find_element_by_xpath('//img[@class="be6sR"]')
		except:
			try:
				image=driver.find_element_by_xpath('//img[@class="_6q-tv"]')
			except:
				return 0
		img_link=image.get_attribute('src')
		try:
			os.mkdir('Dp')
		except:
			pass
		cur = os.getcwd()
		path = cur + "\\Dp\\"  + usr + ".jpg"
		urllib.request.urlretrieve(img_link,path)
		print("Dp saved Successfully  at location: "+path)
		return 1
	except Exception as es:
		print(es)
		return 0
		
	
if __name__ == "__main__":
    print("Please run home_page.py")