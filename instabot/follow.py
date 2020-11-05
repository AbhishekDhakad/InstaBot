from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def followacc(driver,victim):
    driver.get('https://www.instagram.com/%s' % victim)
    sleep(2)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/h2')
        driver.quit()
        return 0
    except:
        try:
            driver.find_element_by_xpath('//*[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]').click()
            print("Account followed")
            driver.quit()
            return 1
        except:
            try:
                driver.find_element_by_xpath('//*[@class="sqdOP  L3NKy   y3zKF     "]').click()
                print("Account Private, Request sent Successfully")
                driver.quit()
                return 2
            except:
                print("You Already Follow this account")
                driver.quit()
                return 3
        
def info(driver,account,page):
    sleep(1)
    driver.get('https://www.instagram.com/%s' % account)
    sleep(2)
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' %page).click()
    txt=driver.find_element_by_xpath('//a[contains(@href, "%s")]' %page).text
    count=int(txt.split()[0])
    print(page," : ",count)
    sleep(2)
    list_h=[]
    print("Getting data... please wait...")
    for i in range(1,count+1):
        src=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]'% i)
        driver.execute_script("arguments[0].scrollIntoView();", src)
        if page=="following":
            if(i%10==0):
                sleep(1)
        else:
            if(i%20==0):
                sleep(1)
        txt=src.text
        name=txt.split()[0]
        list_h.append(name)
    return list_h

def getdata(driver,account,req,loc):
    path=loc+account+"_"+req+".txt"
    file=open(r"%s"%(path,),"w")
    if(req=="followers"):
        followers=info(driver,account,"followers")
        s=0
        for i in followers:
            file.write("%s  "%s+i+"\n")
        file.close()
        print(followers)

    if(req=="following"):
        following=info(driver,account,"following")
        s=0
        for i in following:
            s=s+1
            file.write("%s  "%s+i+"\n")
        file.close()
        print(following)

    if(req=="unfollower"):
        followers=info(driver,account,"followers")
        following=info(driver,account,"following")
        unfollower=[]
        s=0
        for i in following:
            if i not in followers:
                s=s+1
                file.write("%s  "%s+i+"\n")
        print("unfollower  :",s)
        print(unfollower)
    file.close()
    print("Got data")
    driver.quit()
    return 1
