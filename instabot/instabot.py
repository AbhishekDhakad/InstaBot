from time import sleep
import urllib.request
import itertools
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
import Login
import details
import msg
import follow
import datafile

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

try:
	import mysql.connector
except:
	print("mysql connection failed : try after using command pip install mysql.connector and setting up mysql database")

def webd():
	try:
		driver=webdriver.Chrome()
		return driver
	except:
		print('Download ChromeDriver, of same version as of Chrome and place the chromedriver.exe file in Same directory as of this file')
		print('download from here: https://chromedriver.chromium.org/downloads')
		sleep(10)
		quit()

def save_data(victim):
	instalogin()
	datafile.info_list(driver,username)


##################Dp###############

def savedp():
	global screen2
	screen2=Toplevel(screen1)
	screen2.resizable(False,False)
	screen2.title("InstaBot-Dpdownloader")
	screen2.iconbitmap(r"images/icon.ico")
	screen2.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/DP.jpg")
	Label(screen2,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen2,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	title=Label(frame1,text="DP Download",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=120,y=20)

	global txt1,txt2
	
	f_name=Label(frame1,text="Enter their username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=150)
	txt1=Entry(frame1,font=("times new roman",17), bg="lightblue",cursor="hand2")
	txt1.place(x=140,y=210,width=250,height=30)

	username=Label(frame1,text="Enter path, where you want to save:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=290)
	txt2=Entry(frame1,font=("times new roman",17),bg="lightblue",cursor="hand2")
	txt2.place(x=140,y=350,width=250,height=30)

	btn3=Button(screen2,text="Download",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_dp).place(x=860,y=530,width=125,height=40)
	screen2.mainloop()

def verify_dp():
	if txt1.get()=="" or txt2.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen2)
	else:
		dpdownload()


def dpdownload():
	driver=webd()
	victim=txt1.get()
	path=txt2.get()
	var=details.dpdownload(driver,victim,path)
	if(var):
		screen2.destroy()
		messagebox.showinfo("Success","Dp Saved")
	else:
		messagebox.showerror("Error","Enter valid Username or Path")


########bio###################

def savebio():
	global screen3
	screen3=Toplevel(screen1)
	screen3.resizable(False,False)
	screen3.title("InstaBot-Bio Saver")
	screen3.iconbitmap(r"images/icon.ico")
	screen3.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/Bio.jpg")
	Label(screen3,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen3,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	title=Label(frame1,text="Bio Saver",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=120,y=20)

	global txt3,txt4

	f_name=Label(frame1,text="Enter their username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=150)
	txt3=Entry(frame1,font=("times new roman",17), bg="lightblue",cursor="hand2")
	txt3.place(x=140,y=210,width=250,height=30)

	loc=Label(frame1,text="Enter path, where you want to save:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=290)
	txt4=Entry(frame1,font=("times new roman",17),bg="lightblue",cursor="hand2")
	txt4.place(x=140,y=350,width=250,height=30)

	btn3=Button(screen3,text="Save",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_bio).place(x=860,y=530,width=125,height=40)

	screen3.mainloop()

def verify_bio():
	if txt3.get()=="" or txt4.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen3)
	else:
		getbio()

def getbio():
	driver=webd()
	victim=txt3.get()
	path=txt4.get()
	var=details.savebio(driver,victim,path)
	if(var):
		screen3.destroy()
		messagebox.showinfo("Success","Bio Saved")
	else:
		messagebox.showerror("Error","Enter valid username or Path")


####################Info##########

def saveinfo():
	global screen4
	screen4=Toplevel(screen1)
	screen4.resizable(False,False)
	screen4.title("InstaBot-Get Others Details")
	screen4.iconbitmap(r"images/icon.ico")
	screen4.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/info.jpg")
	Label(screen4,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen4,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	title=Label(frame1,text="Save Someone's Info",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=90,y=20)

	global txt5,txt6
	
	f_name=Label(frame1,text="Enter their username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=150)
	txt5=Entry(frame1,font=("times new roman",17), bg="lightblue",cursor="hand2")
	txt5.place(x=140,y=210,width=250,height=30)

	username=Label(frame1,text="Enter path, where you want to save:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=290)
	txt6=Entry(frame1,font=("times new roman",17),bg="lightblue",cursor="hand2")
	txt6.place(x=140,y=350,width=250,height=30)

	global var_chk
	var_chk=IntVar()

	chk=Checkbutton(frame1,text="Want this to save on Database??",variable=var_chk,onvalue=1,offvalue=0,bg="white",fg="black",font=("times new roman",14)).place(x=50,y=400)

	btn3=Button(screen4,text="Save",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_info).place(x=860,y=530,width=125,height=40)

	screen4.mainloop()


def verify_info():
	if txt5.get()=="" or txt6.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen4)
	else:
		getinfo()

def getinfo():
	driver=webd()
	victim=txt5.get()
	path=txt6.get()
	choice=var_chk.get()
	var=datafile.takeinfo(driver,victim,path,choice)
	if(var):
		screen4.destroy()
		messagebox.showinfo("Success","Info Saved")
	else:
		messagebox.showerror("Error","Enter valid username or Path")


################ message #############
def mssg():
	global screen5
	screen5=Toplevel(screen1)
	screen5.resizable(False,False)
	screen5.title("InstaBot-Send Message")
	screen5.iconbitmap(r"images/icon.ico")
	screen5.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/Messsage.jpg")
	Label(screen5,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen5,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=560,y=80,width=700,height=550)

	global usr1,password1,vic1,msg1

	title=Label(frame1,text="Send Message",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	usr=Label(frame1,text="Insta Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=170)
	usr1=Entry(frame1,font=("times new roman",15), bg="lightblue")
	usr1.place(x=50,y=210,width=250,height=30)

	_name=Label(frame1,text="Insta Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=170)
	password1=Entry(frame1,font=("times new roman",15),show="*",bg="lightblue")
	password1.place(x=370,y=210,width=250,height=30)

	label=Label(frame1,text="Their Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=300)
	vic1=Entry(frame1,font=("times new roman",15),bg="lightblue")
	vic1.place(x=50,y=340,width=250,height=30)

	msg=Label(frame1,text="Message:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=300)
	msg1=Entry(frame1,font=("times new roman",15),bg="lightblue")
	msg1.place(x=370,y=340,width=250,height=30)

	btn3=Button(screen5,text="Send",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_msg).place(x=820,y=530,width=125,height=40)
	screen5.mainloop()

def verify_msg():
	if usr1.get()=="" or password1.get()=="" or vic1.get()=="" or msg1.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen5)
	else:
		msgsender()


def msgsender():
	username=usr1.get()
	password=password1.get()
	message=msg1.get()
	victim=vic1.get()
	driver=webd()
	key=Login.loggin(driver, username, password)
	if(key):
		k=msg.sendmsg(driver,victim,message)
		if(k):
			screen5.destroy()
			messagebox.showinfo("Success","Message sent")
		else:
			messagebox.showerror("Error","Invalid Username of Reciever",parent=screen5)
	else:
		driver.quit()
		messagebox.showerror("Error","Invalid Username & Password",parent=screen5)

################# bomber##########################

def bomb():
	global screen6
	screen6=Toplevel(screen1)
	screen6.resizable(False,False)
	screen6.title("InstaBot-Send Message")
	screen6.iconbitmap(r"images/icon.ico")
	screen6.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/Bomber.jpg")
	Label(screen6,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen6,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=560,y=80,width=700,height=550)

	global usr2,password2,vic2,msg2,num2

	title=Label(frame1,text="Message Bomber",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	usr=Label(frame1,text="Insta Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=170)
	usr2=Entry(frame1,font=("times new roman",15), bg="lightblue")
	usr2.place(x=50,y=210,width=250,height=30)

	_name=Label(frame1,text="Insta Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=170)
	password2=Entry(frame1,font=("times new roman",15),show="*",bg="lightblue")
	password2.place(x=370,y=210,width=250,height=30)

	label=Label(frame1,text="Their Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=270)
	vic2=Entry(frame1,font=("times new roman",15),bg="lightblue")
	vic2.place(x=50,y=310,width=250,height=30)

	msg=Label(frame1,text="Message:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=270)
	msg2=Entry(frame1,font=("times new roman",15),bg="lightblue")
	msg2.place(x=370,y=310,width=250,height=30)

	numd=Label(frame1,text="How many?",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=370)
	num2=Entry(frame1,font=("times new roman",15),bg="lightblue")
	num2.place(x=50,y=410,width=250,height=30)

	btn3=Button(screen6,text="Send",font=("calibri",16,"bold"),bg="red",cursor="hand2",command=verify_bomb).place(x=1000,y=520,width=125,height=40)
	screen6.mainloop()

def verify_bomb():
	if usr2.get()=="" or password2.get()=="" or vic2.get()=="" or msg2.get()=="" or num2.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen6)
	else:
		msgbomber()

def msgbomber():
	username=usr2.get()
	password=password2.get()
	message=msg2.get()
	victim=vic2.get()
	num=int(num2.get())
	driver=webd()
	key=Login.loggin(driver, username, password)
	if(key):
		k=msg.blast(driver,victim,message,num)
		if(k):
			screen6.destroy()
			messagebox.showinfo("Success","Message sent")
		else:
			messagebox.showerror("Error","Invalid Username of Reciever",parent=screen6)
	else:
		driver.quit()
		messagebox.showerror("Error","Invalid Username & Password",parent=screen6)


#################  send req ######################

def sendreq():
	global screen7
	screen7=Toplevel(screen1)
	screen7.resizable(False,False)
	screen7.title("InstaBot-Send Message")
	screen7.iconbitmap(r"images/icon.ico")
	screen7.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/Request.jpg")
	Label(screen7,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen7,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=560,y=80,width=700,height=550)

	global usr3,password3,vic3

	title=Label(frame1,text="Follow Someone",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	usr=Label(frame1,text="Insta Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=170)
	usr3=Entry(frame1,font=("times new roman",15), bg="lightblue")
	usr3.place(x=50,y=210,width=250,height=30)

	_name=Label(frame1,text="Insta Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=170)
	password3=Entry(frame1,font=("times new roman",15),show="*",bg="lightblue")
	password3.place(x=370,y=210,width=250,height=30)

	label=Label(frame1,text="Their Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=300)
	vic3=Entry(frame1,font=("times new roman",15),bg="lightblue")
	vic3.place(x=50,y=340,width=250,height=30)

	btn3=Button(screen7,text="Send Req",font=("calibri",16,"bold"),bg="pink",cursor="hand2",command=verify_req).place(x=1010,y=500,width=125,height=40)
	screen7.mainloop()

def verify_req():
	if usr3.get()=="" or password3.get()=="" or vic3.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen6)
	else:
		req()

def req():
	username=usr3.get()
	password=password3.get()
	victim=vic3.get()
	driver=webd()
	key=Login.loggin(driver, username, password)
	if(key):
		k=follow.followacc(driver,victim)
		if(k==1):
			screen7.destroy()
			messagebox.showinfo("Success","Account Followed")
		elif(k==2):
			screen7.destroy()
			messagebox.showinfo("Account Private","Request send Successfully")
		elif(k==3):
			screen7.destroy()
			messagebox.showerror("Error","Already Followed")
		else:
			messagebox.showerror("Error","Enter valid account to follow",parent=screen7)
	else:
		driver.quit()
		messagebox.showerror("Error","Invalid Username & Password",parent=screen7)


##################### follow/unfollow ##############


def getlist():
	global screen8
	screen8=Toplevel(screen1)
	screen8.resizable(False,False)
	screen8.title("InstaBot-Get follower/unfollower")
	screen8.iconbitmap(r"images/icon.ico")
	screen8.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/Follow.jpg")
	Label(screen8,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen8,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=560,y=80,width=700,height=550)

	global usr4,password4,page4,path4

	title=Label(frame1,text="Follower/Unfollower",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	usr=Label(frame1,text="Insta Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=170)
	usr4=Entry(frame1,font=("times new roman",15), bg="lightblue")
	usr4.place(x=50,y=210,width=250,height=30)

	_name=Label(frame1,text="Insta Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=170)
	password4=Entry(frame1,font=("times new roman",15),show="*",bg="lightblue")
	password4.place(x=370,y=210,width=250,height=30)

	label=Label(frame1,text="Which list you want ?",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=300)
	page4=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
	page4['values']=("--select--","followers","following","unfollower")
	page4.place(x=50,y=340,width=250,height=30)
	page4.current(0)

	msg=Label(frame1,text="Enter path, where you want to save:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=350,y=300)
	path4=Entry(frame1,font=("times new roman",15),bg="lightblue")
	path4.place(x=370,y=340,width=250,height=30)

	btn3=Button(screen8,text="Get",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_localsave).place(x=820,y=530,width=125,height=40)
	screen8.mainloop()

def verify_localsave():
	if usr4.get()=="" or password4.get()=="" or page4.get()=="" or path4.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen8)
	else:
		localsave()

def localsave():
	username=usr4.get()
	password=password4.get()
	page=page4.get()
	path=path4.get()
	driver=webd()
	key=Login.loggin(driver, username, password)
	if(key):
		k=follow.getdata(driver,username,page,path)
		if(k):
			screen8.destroy()
			messagebox.showinfo("Success","List Saved")
		else:
			messagebox.showerror("Error","Error Occured",parent=screen8)
	else:
		driver.quit()
		messagebox.showerror("Error","Invalid Username & Password",parent=screen8)


########################## upload list ################

def uploadlist():
	global screen9
	screen9=Toplevel(screen1)
	screen9.resizable(False,False)
	screen9.title("InstaBot-Upload connection list")
	screen9.iconbitmap(r"images/icon.ico")
	screen9.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/upload.jpg")
	Label(screen9,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen9,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	title=Label(frame1,text="Upload Data",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=120,y=20)

	global usr5,password5

	f_name=Label(frame1,text="Insta Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=150)
	usr5=Entry(frame1,font=("times new roman",17), bg="lightblue")
	usr5.place(x=140,y=210,width=250,height=30)

	loc=Label(frame1,text="Insta Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=290)
	password5=Entry(frame1,font=("times new roman",17),bg="lightblue",show="*")
	password5.place(x=140,y=350,width=250,height=30)

	btn3=Button(screen9,text="Upload",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_upload).place(x=860,y=530,width=125,height=40)

	screen9.mainloop()

def verify_upload():
	if usr5.get()=="" or password5.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen9)
	else:
		upload()

def upload():
	username=usr5.get()
	password=password5.get()
	driver=webd()
	key=Login.loggin(driver, username, password)
	if(key):
		k=datafile.info_list(driver,username)
		if(k==1):
			screen9.destroy()
			messagebox.showinfo("Success","Data Uploaded")
		else:
			messagebox.showerror("Error","Error Occured",parent=screen9)
	else:
		driver.quit()
		messagebox.showerror("Error","Invalid Username & Password",parent=screen9)


def aboutus():
	global screen10
	screen10=Toplevel(screen1)
	screen10.resizable(False,False)
	screen10.title("InstaBot-About Us")
	screen10.iconbitmap(r"images/icon.ico")
	screen10.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/About_us_page.jpg")
	Label(screen10,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(screen10,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=500,y=80,width=237,height=580)

	frame2=Frame(screen10,bg="white",highlightthickness=3)
	frame2.config(highlightbackground="gray")
	frame2.place(x=767,y=80,width=237,height=580)

	frame3=Frame(screen10,bg="white",highlightthickness=3)
	frame3.config(highlightbackground="gray")
	frame3.place(x=1034,y=80,width=237,height=580)

	k=ImageTk.PhotoImage(file="images/abhishek.jpg")
	Label(frame1,image=k).place(x=20,y=20,width=197,height=197)
	Label(frame1,text="Abhishek",font=("times new roman",25,"bold","italic","underline"),fg="black",bg="white").place(x=50,y=230)

	Label(frame1,text="- Wrote code for Automation",font=("times new roman",14),fg="black",bg="white").place(x=0,y=290)
	Label(frame1,text="- Wrote code for Scrapping\ndata from Instagram",font=("times new roman",14),fg="black",bg="white").place(x=0,y=315)
	Label(frame1,text="- Connected code with \n Tkinter and Database",font=("times new roman",14),fg="black",bg="white").place(x=0,y=360)
	Label(frame1,text="Skills",font=("times new roman",18,"bold"),fg="black",bg="white").place(x=0,y=410)
	Label(frame1,text="- Cpp, DSA, Python, SQL,\nCompetitive Programming, \nWeb Scrapping,Web dev",font=("times new roman",14),fg="black",bg="white").place(x=0,y=440)
	in1=ImageTk.PhotoImage(file="images/insta.jpg")
	m1=ImageTk.PhotoImage(file="images/mail.jpg")
	ln1=ImageTk.PhotoImage(file="images/linkdin.jpg")
	Button(frame1,image=in1,cursor="hand2",command=insta1,bd=0).place(x=33,y=525,width=35,height=35)
	Button(frame1,image=m1,cursor="hand2",command="",bd=0).place(x=101,y=525,width=35,height=35)
	Button(frame1,image=ln1,cursor="hand2",command=linkedin1,bd=0).place(x=169,y=525,width=35,height=35)
	

	k2=ImageTk.PhotoImage(file="images/tamana.jpg")
	Label(frame2,image=k2).place(x=20,y=20,width=197,height=197)
	Label(frame2,text="Tamana",font=("times new roman",25,"bold","italic","underline"),fg="black",bg="white").place(x=60,y=230)
	Label(frame2,text="- Wrote code for Tkinter",font=("times new roman",14),fg="black",bg="white").place(x=0,y=290)
	Label(frame2,text="- Wrote code for Login\nand Registration Page",font=("times new roman",14),fg="black",bg="white").place(x=0,y=315)
	Label(frame2,text="- Suggested Designs for \npages and new features",font=("times new roman",14),fg="black",bg="white").place(x=0,y=360)
	Label(frame2,text="Skills",font=("times new roman",18,"bold"),fg="black",bg="white").place(x=0,y=410)
	Label(frame2,text="- Content Writing, Python,\nC, English Proficiency",font=("times new roman",14),fg="black",bg="white").place(x=0,y=440)
	in2=ImageTk.PhotoImage(file="images/insta.jpg")
	m2=ImageTk.PhotoImage(file="images/mail.jpg")
	ln2=ImageTk.PhotoImage(file="images/linkdin.jpg")
	Button(frame2,image=in2,cursor="hand2",command=insta2,bd=0).place(x=33,y=525,width=35,height=35)
	Button(frame2,image=m2,cursor="hand2",command="",bd=0).place(x=101,y=525,width=35,height=35)
	Button(frame2,image=ln2,cursor="hand2",command=linkedin2,bd=0).place(x=169,y=525,width=35,height=35)

	k3=ImageTk.PhotoImage(file="images/sufyan.jpg")
	Label(frame3,image=k3).place(x=20,y=20,width=197,height=197)
	Label(frame3,text="Sufiyan",font=("times new roman",25,"bold","italic","underline"),fg="black",bg="white").place(x=60,y=230)
	Label(frame3,text="- Wrote Queries for Database",font=("times new roman",14),fg="black",bg="white").place(x=0,y=290)
	Label(frame3,text="- Created InstaBot Icons and \nTamplates for background ",font=("times new roman",14),fg="black",bg="white").place(x=0,y=315)
	Label(frame3,text="- Wrote Module for \nDp Downloader",font=("times new roman",14),fg="black",bg="white").place(x=0,y=360)
	Label(frame3,text="Skills",font=("times new roman",18,"bold"),fg="black",bg="white").place(x=0,y=410)
	Label(frame3,text="- Ethical Hacking,Python,\nWeb & Android Penetration \nTester, Basic Linux",font=("times new roman",14),fg="black",bg="white").place(x=0,y=440)
	in3=ImageTk.PhotoImage(file="images/insta.jpg")
	m3=ImageTk.PhotoImage(file="images/mail.jpg")
	ln3=ImageTk.PhotoImage(file="images/linkdin.jpg")
	Button(frame3,image=in3,cursor="hand2",command=insta3,bd=0).place(x=33,y=525,width=35,height=35)
	Button(frame3,image=m3,cursor="hand2",command="",bd=0).place(x=101,y=525,width=35,height=35)
	Button(frame3,image=ln3,cursor="hand2",command=linkedin3,bd=0).place(x=169,y=525,width=35,height=35)

	screen10.mainloop()

def insta1():
	driver=webdriver.Chrome()
	url="https://www.instagram.com/abhishek.dhakad_/"
	driver.get(url)

def insta2():
	driver=webdriver.Chrome()
	url="https://www.instagram.com/tamana_1212/"
	driver.get(url)

def insta3():
	driver=webdriver.Chrome()
	url="https://www.instagram.com/sufyan.gouri/"
	driver.get(url)

def linkedin1():
	driver=webdriver.Chrome()
	url="https://www.linkedin.com/in/abhishek-dhakad-003740192"
	driver.get(url)

def linkedin2():
	driver=webdriver.Chrome()
	url="https://www.linkedin.com/in/tamana-sharma-872211192"
	driver.get(url)

def linkedin3():
	driver=webdriver.Chrome()
	url="https://in.linkedin.com/in/sufiyan-gouri-7a73a8180"
	driver.get(url)

def bot():
	global screen1
	screen1=Tk()
	screen1.resizable(False,False)
	screen1.title("InstaBot: Main Page")
	screen1.iconbitmap(r"images/icon.ico")
	screen1.geometry("1350x700+25+100")
	bg=ImageTk.PhotoImage(file="images/bg3.jpg")
	bg1=Label(screen1,image=bg).place(relwidth=1,relheight=1)
	frame1=Frame(screen1,bg="white",highlightthickness=2)
	frame1.config(highlightbackground="gray")
	frame1.place(x=500,y=100,width=300,height=530)

	Label(frame1, text = "Basic", fg = "black" ,font = ("bree serif",22,"bold"),bg="white").place(x=20,y=20,width=75,height=25)

	temp=Button(screen1,text="DP",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=savedp).place(x=580,y=230,width=125,height=40)
	temp=Button(screen1,text="Bio",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=savebio).place(x=580,y=390,width=125,height=40)
	temp=Button(screen1,text="Info",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=saveinfo).place(x=580,y=550,width=125,height=40)

	frame2=Frame(screen1,bg="white",highlightthickness=2)
	frame2.config(highlightbackground="gray")
	frame2.place(x=850,y=100,width=450,height=530)

	Label(frame2, text = "Advance", fg = "black" ,font = ("bree serif",22,"bold"),bg="white").place(x=20,y=20,width=150,height=25)

	temp=Button(screen1,text="Message",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=mssg).place(x=1110,y=210,width=125,height=40)
	temp=Button(screen1,text="Bomber",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=bomb).place(x=890,y=300,width=125,height=40)
	temp=Button(screen1,text="send-req",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=sendreq).place(x=1110,y=390,width=125,height=40)
	temp=Button(screen1,text="foll/unfoll",font=("calibri",14,"bold"),bg="violet",cursor="hand2",command=getlist).place(x=890,y=470,width=125,height=40)
	temp=Button(screen1,text="upload",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=uploadlist).place(x=1110,y=550,width=125,height=40)
	temp=Button(screen1,text="About Us",font=("calibri",16,"bold"),bg="navy",fg="yellow",cursor="hand2",command=aboutus).place(x=1140,y=80,width=125,height=40)

	screen1.mainloop()
