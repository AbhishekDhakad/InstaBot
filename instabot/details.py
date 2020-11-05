from selenium import webdriver
from time import sleep
import urllib.request

def savebio(driver,victim,loc):
    try:
    	url='https://www.instagram.com/'+victim
    	driver.get(url)
    	txt=driver.find_element_by_xpath('//*[@class="-vDIg"]').text
    	path=loc + victim + ".txt"
    	bio=""
    	for e in txt:
    	    if(ord(e)<=128):
    	    	bio=bio+e
    	    else:
    	    	bio=bio+"*"
    	file=open(r"%s"%(path,),"w")
    	file.write(bio)
    	file.close()
    	driver.quit()
    	print("_____Bio saved SUCCESSFULLY_____")
    	print("At location --->>>"+path)
    	return 1
    except Exception as es:
    	print(es)
    	return 0

def dpdownload(driver,victim,loc):
	try:
		url='https://www.instagram.com/'+victim
		driver.get(url)
		try:
			image=driver.find_element_by_xpath('//img[@class="be6sR"]')
		except:
			image=driver.find_element_by_xpath('//img[@class="_6q-tv"]')
		img_link=image.get_attribute('src')
		path=loc + victim + ".jpg"
		urllib.request.urlretrieve(img_link,path)
		driver.quit()
		print("__________Dp saved Successfully_________ \n\n ______at loc -->> : "+path)
		return 1
	except Exception as es:
		print(es)
		return 0
	
