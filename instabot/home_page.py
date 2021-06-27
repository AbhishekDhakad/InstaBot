from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from instabot import bot
import Login
from time import sleep
import os

try:
	from selenium import webdriver
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By 
except:
	print("Requirment not Satisfied")
	choice=input("Do you want to install selenium(y/n): ")
	if(choice.lower()=="y"):
		os.system("python -m pip install selenium")
	else:
		print("Download necessary files, using command ( python -m pip install selenium )")
	sleep(5)
	quit()

def webd():
	try:
		browser=webdriver.Chrome()
		return browser
	except:
		print('Download ChromeDriver, of same version as of Chrome and place the chromedriver.exe file in Same directory as of this file')
		print('download from here: https://chromedriver.chromium.org/downloads')
		sleep(10)
		quit()


def login_page():
	global screen3
	screen3=Tk()
	screen3.resizable(False,False)
	screen3.title("InstaBot-Login")
	screen3.iconbitmap(r"images/icon.ico")

	w = screen3.winfo_screenwidth()
	h = screen3.winfo_screenheight()

	screen3.geometry(f"{w}x{h}+0+0")

	frame3=Frame(screen3,bg="white",highlightthickness=3)
	frame3.config(highlightbackground="gray")
	frame3.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/Login_Page.jpg")
	reg1=Label(frame3,image=reg).place(relwidth=1,relheight=1)

	global usr,pwd
	usr=Entry(frame3,font=("times new roman",15),bg="lightgray")
	usr.place(x=741,y=310,width=390,height=35)

	pwd=Entry(frame3,font=("times new roman",15),show="*",bg="lightgray")
	pwd.place(x=741,y=410,width=390,height=35)

	btn3=Button(frame3,text="Login",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_login).place(x=875,y=512,width=125,height=40)
	screen3.mainloop()

	



def verify_login():
	if usr.get()=="" or pwd.get()=="":
		messagebox.showerror("Error","All Field required",parent=screen3)
	else:
		try:
			global driver
			driver = webd()
			chk = Login.chk_login(driver,usr.get(),pwd.get())
			if(chk):
				messagebox.showinfo("Success","Welcome",parent=screen3)
				activate_bot()
			else:
				messagebox.showerror("Error","Invalid Username & Password",parent=screen3)

		except Exception as es:
			messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=screen3)


def activate_bot():
	#if we destroy screen first then get function will not work
	var1 = usr.get()

	screen3.destroy()
	bot(driver,var1)

login_page()