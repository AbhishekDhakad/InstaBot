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
        return 0
    except:
        try:
            driver.find_element_by_xpath('//*[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]').click()
            print("Account followed")
            return 1
        except:
            try:
                driver.find_element_by_xpath('//*[@class="sqdOP  L3NKy   y3zKF     "]').click()
                print("Account Private, Request sent Successfully")
                return 1
            except:
                print("You Already Follow this account")
                return 1
        

def unfollowacc(driver,usrlist):
    for usr in usrlist:
        driver.get('https://www.instagram.com/%s' % usr)
        sleep(2)
        try:
            driver.find_element_by_css_selector("button[class='_5f5mN    -fzfL     _6VtSN     yZn4P   ']").click()
            sleep(1)
            driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
            print("Unfollowed")
        except:
            try:
                driver.find_element_by_xpath('//button[text()="Requested"]').click()
                print("Request Cancelled")
            except:
                print("You doesn't follow this account")


def info(driver,account,page):
    sleep(1)
    driver.get('https://www.instagram.com/%s' % account)
    sleep(2)
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' %page).click()
    txt=driver.find_element_by_xpath('//a[contains(@href, "%s")]' %page).text
    count=int(txt.split()[0])
    print(page," : ",count)
    sleep(3)
    list_h=[]
    print("Getting data... please wait...")
    for i in range(1,count+1):
        src=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]'% i)
        driver.execute_script("arguments[0].scrollIntoView();", src)
        if page=="following":
            if(i%7==0):
                sleep(2)
        else:
            if(i%7==0):
                sleep(2)
        txt=src.text
        name=txt.split()[0]
        list_h.append(name)
    return list_h

def getdata(driver,account,req):

    if(req=="followers"):

        followers=info(driver,account,"followers")
        print("Got data")
        driver.minimize_window()
        return followers

    if(req=="following"):

        following=info(driver,account,"following")
        print("Got data")
        driver.minimize_window()
        return following

    if(req=="unfollower"):

        followers=info(driver,account,"followers")
        following=info(driver,account,"following")
        unfollower=[]
        s=0
        for i in following:
            if i not in followers:
                s=s+1
                unfollower.append(i)
        print("unfollower  :",s)
        print("Got data")
        driver.minimize_window()
        return unfollower


    
