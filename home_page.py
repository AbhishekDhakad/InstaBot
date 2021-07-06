from tkinter import *
import tkinter as tk
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
	global root
	root=Tk()
	root.resizable(False,False)
	root.title("InstaBot-Login")
	try:
		root.iconbitmap(r"images/icon.ico")
	except:
		pass

	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()

	root.geometry(f"{w}x{h}+0+0")
	root.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(root,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)

	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(root,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(root,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)

	Label(root,text="Welcome to Instapy",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-690,y=50)
	Label(root,text="The Instabot",font=("Helvetica",30),bg="#1b3b5f",fg="#EDEDED").place(x=w-570,y=125)

	frame = Frame(root,bg="#455566")
	frame.place(x=w-750,y=240,width=600,height=500)

	user = ImageTk.PhotoImage(file="images/user.png")
	Label(frame,image=user,bg="#455566").place(x=236,y=20,width=128,height=128)

	global usr,pwd

	usr = tk.Entry(frame,font=("calibri",20),bg="#556080",fg="#FFFFFF",highlightthickness=0,borderwidth=0,justify='center')
	usr.insert(0,"Username")

	def clback(event):             #for erasing what we have in entry box
		usr.delete(0,"end")
		return None

	usr.bind("<Button-1>",clback)

	usr.place(x=160,y=220,height=40,width=280)

	usr1 = ImageTk.PhotoImage(file="images/1.png")
	Label(frame,image=usr1,bg="#07254b").place(x=120,y=220,height=40,width=40)


	pwd = tk.Entry(frame,font=("calibri",20),show="*",bg="#556080",fg="#FFFFFF",highlightthickness=0,borderwidth=0,justify='center')
	pwd.insert(0,"********")

	def cllback(event):
		pwd.delete(0,"end")
		return None

	pwd.bind("<Button-1>",cllback)

	pwd.place(x=160,y=290,height=40,width=280)

	pwd1 = ImageTk.PhotoImage(file="images/2.png")
	Label(frame,image=pwd1,bg="#07254b").place(x=120,y=290,height=40,width=40)


	btn = ImageTk.PhotoImage(file="images/loginbtn.png")
	Button(frame,image=btn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_login).place(x=150,y=390,width=300,height=65)

	root.state('zoomed')
	root.mainloop()



def verify_login():
	if usr.get()=="" or pwd.get()=="" or usr.get()=="Username" or pwd.get()=="********":
		messagebox.showerror("Error","All Field required",parent=root)
	else:
		try:
			global driver
			driver = webd()
			chk = Login.chk_login(driver,usr.get(),pwd.get())
			if(chk):
				messagebox.showinfo("Success","Welcome",parent=root)
				activate_bot()
			else:
				messagebox.showerror("Error","Invalid Username & Password",parent=root)

		except Exception as es:
			messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=root)


def activate_bot():
	#if we destroy screen first then get function will not work
	var1 = usr.get()

	root.destroy()
	bot(driver,var1)

login_page()