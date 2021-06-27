from time import sleep
from tkinter import *
from typing import Pattern
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
from tkinter import filedialog as fd
import itertools
import Login
import details
import msg
import follow
import datafile
import webbrowser
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 


##################Dp###############

def savedp():
	global screen2
	screen2=Toplevel(screen1)
	screen2.resizable(False,False)
	screen2.title("InstaBot-Dpdownloader")
	try:
		screen2.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen2.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen2,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/DP.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)

	frame1=Frame(framex,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	
	global num1,dpusr

	Label(frame1,text="DP Download",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	Label(frame1,text="Number of Person?",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=150)
	num1=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
	num1['values']=("1","2","3","4","5","6","7","8","9","10")
	num1.place(x=50,y=190,width=250,height=30)
	num1.current(0)

	Label(frame1,text="Usernames (seprated by space):",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=300)
	dpusr=Entry(frame1,font=("times new roman",15),bg="lightblue")
	dpusr.place(x=50,y=340,width=250,height=30)

	Button(framex,text="Download",font=("calibri",16,"bold"),bg="pink",cursor="hand2",command=verify_dp).place(x=1010,y=500,width=125,height=40)

	screen2.mainloop()

def verify_dp():
	if dpusr.get()=="" or num1.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen2)
	else:
		dpdownload()


def dpdownload():
	vic=dpusr.get().split()
	driver.set_window_size(800,950)
	for usr in vic:
		k=details.dpdownload(driver,usr)
		if(k!=1):
			print(usr," is invalid")
	driver.minimize_window()
	messagebox.showinfo("Success","Done")
	screen2.destroy()


########bio###################

def savebio():
	global screen3
	screen3=Toplevel(screen1)
	screen3.resizable(False,False)
	screen3.title("InstaBot-Bio Saver")
	try:
		screen3.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen3.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen3,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/Bio.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(framex,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	global biousr,bionum

	Label(frame1,text="Save Bio",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	Label(frame1,text="Number of Person?",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=150)
	bionum=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
	bionum['values']=("1","2","3","4","5","6","7","8","9","10")
	bionum.place(x=50,y=190,width=250,height=30)
	bionum.current(0)

	Label(frame1,text="Usernames (seprated by space):",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=300)
	biousr=Entry(frame1,font=("times new roman",15),bg="lightblue")
	biousr.place(x=50,y=340,width=250,height=30)

	Button(framex,text="Save",font=("calibri",16,"bold"),bg="pink",cursor="hand2",command=verify_bio).place(x=1010,y=500,width=125,height=40)

	screen3.mainloop()

def verify_bio():
	if biousr.get()=="" or bionum.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen3)
	else:
		getbio()

def getbio():
	vic=biousr.get().split()
	driver.set_window_size(800,950)
	for usr in vic:
		k=details.savebio(driver,usr)
		if(k!=1):
			print(usr," is invalid")
	driver.minimize_window()
	messagebox.showinfo("Success","Done")
	screen3.destroy()


####################Info##########

def viewinfo():
	global screen4
	screen4=Toplevel(screen1)
	screen4.resizable(False,False)
	screen4.title("InstaBot-Get Others Details")
	try:
		screen4.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen4.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen4,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/info.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)

	global frameview

	frameview=Frame(framex,bg="white",highlightthickness=3)
	frameview.config(highlightbackground="gray")
	frameview.place(x=660,y=80,width=550,height=550)

	global viewusr

	Label(frameview,text="View User",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=20)
	
	Label(frameview,text="Usernames (seprated by space):",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=70,y=120)

	viewusr=Entry(frameview,font=("times new roman",15),bg="lightblue")
	viewusr.place(x=100,y=170,width=300,height=45)


	global viewlist
	scroll = Scrollbar(frameview,orient=VERTICAL)

	viewlist = Listbox(frameview,bg="lightblue",yscrollcommand=scroll.set)
	scroll.config(command=viewlist.yview)
	viewlist.place(x=100,y=270,width=300,height=170)
	scroll.place(x=395,y=270,width=20,height=170)

	Button(frameview,text="Get",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_info).place(x=120,y=470,width=120,height=40)

	Button(frameview,text="Clear",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=clear_info).place(x=250,y=470,width=120,height=40)

	screen4.mainloop()


def verify_info():
	if viewusr.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen4)
	else:
		getinfo()

def getinfo():
	vic=viewusr.get().split()
	driver.set_window_size(800,950)
	temp = ["Name      ","followers","following","posts     "]
	for usr in vic:
		viewlist.insert(END,"         "+str(usr)+"\n")
		k=datafile.takeinfo(driver,usr)
		if(k==0):
			print(usr," is invalid")
		else:
			for (i,j) in zip(k,temp):
				viewlist.insert(END, j +"  -  "+ i +"\n")
			viewlist.insert(END,"\n\n")
	driver.minimize_window()
	messagebox.showinfo("Success","text file saved",parent=screen4)

def clear_info():
	viewlist.delete(0,END)



################ message #############

def mssg():
	global screen5
	screen5=Toplevel(screen1)
	screen5.resizable(False,False)
	screen5.title("InstaBot-Send Message")
	try:
		screen5.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen5.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen5,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700) 

	reg=ImageTk.PhotoImage(file="images/Messsage.jpg")

	Label(framex,image=reg).place(relwidth=1,relheight=1)

	frame1=Frame(framex,bg="white")
	# frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	title=Label(frame1,text="Send Message",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=120,y=20)

	global usr1,msg1

	label=Label(frame1,text="Enter their username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=150)
	usr1=Entry(frame1,font=("times new roman",17), bg="lightblue",cursor="hand2")
	usr1.place(x=140,y=210,width=250,height=30)

	msg=Label(frame1,text="Message:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=300)
	msg1=Entry(frame1,font=("times new roman",17),bg="lightblue",cursor="hand2")
	msg1.place(x=140,y=350,width=250,height=30)

	btn3=Button(framex,text="Send",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_msg).place(x=860,y=530,width=125,height=40)

	screen5.mainloop()

def verify_msg():
	if usr1.get()=="" or msg1.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen5)
	else:
		msgsender()


def msgsender():
	message=msg1.get()
	victim=usr1.get()
	driver.set_window_size(800,950)
	k=msg.sendmsg(driver,victim,message)

	if(k):
		screen5.destroy()
		messagebox.showinfo("Success","Message sent")

	else:
		messagebox.showerror("Error","Invalid Username of Reciever",parent=screen5)
	

################# bomber##########################

def bomb():
	global screen6
	screen6=Toplevel(screen1)
	screen6.resizable(False,False)
	screen6.title("InstaBot-Send Message")
	try:
		screen6.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen6.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen6,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/Bomber.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)

	frame1=Frame(framex,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	global usr2,msg2,num2

	title=Label(frame1,text="Message Bomber",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	label=Label(frame1,text="Enter their username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=140)
	usr2=Entry(frame1,font=("times new roman",17), bg="lightblue",cursor="hand2")
	usr2.place(x=140,y=190,width=250,height=30)

	msg=Label(frame1,text="Message:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=250)
	msg2=Entry(frame1,font=("times new roman",17),bg="lightblue",cursor="hand2")
	msg2.place(x=140,y=290,width=250,height=30)

	numd=Label(frame1,text="How many?",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=370)
	num2=Entry(frame1,font=("times new roman",15),bg="lightblue")
	num2.place(x=140,y=410,width=80,height=30)

	btn3=Button(framex,text="Send",font=("calibri",16,"bold"),bg="red",cursor="hand2",command=verify_bomb).place(x=1020,y=510,width=125,height=40)
	screen6.mainloop()

def verify_bomb():
	if usr2.get()=="" or msg2.get()=="" or num2.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen6)
	else:
		msgbomber()

def msgbomber():
	message=msg2.get()
	victim=usr2.get()
	num=int(num2.get())
	driver.set_window_size(800,950)
	
	k=msg.blast(driver,victim,message,num)
	if(k):
		screen6.destroy()
		messagebox.showinfo("Success","Message sent")
	else:
		messagebox.showerror("Error","Invalid Username of Reciever",parent=screen6)


#################  send req ######################

def sendreq():
	global screen7
	screen7=Toplevel(screen1)
	screen7.resizable(False,False)
	screen7.title("InstaBot-Send Message")
	try:
		screen7.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen7.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen7,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/Request.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)

	frame1=Frame(framex,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=660,y=80,width=550,height=550)

	global num3,usr3

	Label(frame1,text="Follow People",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=150,y=35)

	Label(frame1,text="Number of Person?",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=150)
	num3=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
	num3['values']=("1","2","3","4","5","6","7","8","9","10")
	num3.place(x=50,y=190,width=250,height=30)
	num3.current(0)

	Label(frame1,text="Usernames (seprated by space):",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=300)
	usr3=Entry(frame1,font=("times new roman",15),bg="lightblue")
	usr3.place(x=50,y=340,width=250,height=30)

	Button(framex,text="Send Req",font=("calibri",16,"bold"),bg="pink",cursor="hand2",command=verify_req).place(x=1010,y=500,width=125,height=40)
	screen7.mainloop()

def verify_req():
	if usr3.get()=="" or num3.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen6)
	else:
		req()

def req():
	victim=usr3.get().split()
	driver.set_window_size(800,950)
	for vic in victim:
		k=follow.followacc(driver,vic)
		if(k!=1):
			print(k," is invalid")
	driver.minimize_window()
	screen7.destroy()
	messagebox.showinfo("Success","Done")
	


##################### follow/unfollow ##############


def getlist():
	global screen8
	screen8=Toplevel(screen1)
	screen8.resizable(False,False)
	screen8.title("InstaBot-Get follower/unfollower")
	try:
		screen8.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen8.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen8,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/Follow.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)

	global framelist

	framelist=Frame(framex,bg="white",highlightthickness=3)
	framelist.config(highlightbackground="gray")
	framelist.place(x=660,y=80,width=550,height=550)

	global usr4,password4,page4

	Label(framelist,text="Follower/Unfollower",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=70,y=20)

	
	Label(framelist,text="Which list you want ?",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=30,y=120)
	page4=ttk.Combobox(framelist,font=("times new roman",13),state="readonly",justify=CENTER)
	page4['values']=("--select--","followers","following","unfollower")
	page4.place(x=120,y=160,width=250,height=30)
	page4.current(0)

	global mylist
	scroll = Scrollbar(framelist,orient=VERTICAL)

	mylist = Listbox(framelist,bg="lightblue",yscrollcommand=scroll.set)
	scroll.config(command=mylist.yview)
	mylist.place(x=100,y=270,width=300,height=170)
	scroll.place(x=395,y=270,width=20,height=170)

	Button(framelist,text="Get",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_localsave).place(x=150,y=470,width=120,height=40)
	screen8.mainloop()

def verify_localsave():
	if page4.get()=="--select--":
		messagebox.showerror("Error","Select one",parent=screen8)
	else:
		localsave()

def localsave():
	page=page4.get()
	driver.set_window_size(800,950)
	k = follow.getdata(driver,username,page)

	mylist.delete(0,"end")
	mylist.insert("end","        %s"%page.upper())
	mylist.insert("end","\n")

	c=0
	for element in k:
		c=c+1
		mylist.insert("end",element)

	mylist.insert(1,"total  -   %s"%c)

	messagebox.showinfo("Success","Done",parent=screen8)
	btn = Button(framelist,text="save",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=savelist)
	btn.place(x=275,y=470,width=125,height=40)
	
	
def savelist():

	txt_file = fd.asksaveasfile(title="Save text file",filetypes=[("text file","*.txt")],initialdir=os.getcwd(),mode='w')
	stuff = mylist.get(0,END)
	for line in stuff:
		txt_file.write(line)
		txt_file.write("\n")
	txt_file.close()
	messagebox.showinfo("Success","List saved",parent=screen8)
	

########################## unfollow list ################

def unfollow():
	global screen9
	screen9=Toplevel(screen1)
	screen9.resizable(False,False)
	screen9.title("InstaBot-Unfollow Users")
	try:
		screen9.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen9.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen9,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/upload.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)

	global frametxt
	frametxt=Frame(framex,bg="white",highlightthickness=3)
	frametxt.config(highlightbackground="gray")
	frametxt.place(x=660,y=80,width=550,height=550)

	Label(frametxt,text="Unfollow Users",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=100,y=20)

	Label(frametxt,text="Open text file containing Username list",font=("times new roman",15),fg="black",bg="white").place(x=100,y=120)

	btn = Button(frametxt,text="Open File",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=open_file)
	btn.place(x=200,y=150,width=125,height=40)

	Label(frametxt,text="- - - - OR - - - -",font=("times new roman",25,"bold"),fg="black",bg="white").place(x=160,y=200)

	Label(frametxt,text="Write Usernames seprated by line",font=("times new roman",15),fg="black",bg="white").place(x=100,y=250)

	global text_box

	scroll = Scrollbar(frametxt,orient=VERTICAL)

	text_box = Text(frametxt,bg="lightblue",yscrollcommand=scroll.set)
	scroll.config(command=text_box.yview)
	text_box.place(x=100,y=290,width=300,height=160)
	scroll.place(x=395,y=290,width=20,height=160)

	Button(frametxt,text="Unfollow",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_unfollow).place(x=200,y=470,width=125,height=40)

	screen9.mainloop()

def open_file():
	file = fd.askopenfile(title="Open text file",filetypes=[("text file","*.txt")],initialdir=os.getcwd,mode='r',parent=frametxt)
	stuff = file.readlines()
	cnt = 0
	for line in stuff:
		cnt += 1
		if(cnt > 4):
			text_box.insert(END,line)
	file.close()

def verify_unfollow():
	lst = text_box.get("1.0",END).splitlines()
	if lst == "":
		messagebox.showerror("Error","All Feild required",parent=screen9)
	else:
		unfollow_usr(lst)

def unfollow_usr(lst):
	driver.set_window_size(800,950)
	follow.unfollowacc(driver,lst)
	driver.minimize_window()
	messagebox.showinfo("Success","You did't follow them now",parent=screen9)


def contactme():
	global screen10
	screen10=Toplevel(screen1)
	screen10.resizable(False,False)
	screen10.title("InstaBot-Contact Me")
	try:
		screen10.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen10.geometry(f"{w}x{h}+0+0")

	framex=Frame(screen10,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	reg=ImageTk.PhotoImage(file="images/About_us_page.jpg")
	Label(framex,image=reg).place(relwidth=1,relheight=1)
	frame1=Frame(framex,bg="white",highlightthickness=3)
	frame1.config(highlightbackground="gray")
	frame1.place(x=510,y=60,width=741,height=580)

	

	

	k=ImageTk.PhotoImage(file="images/abhishek.jpg")
	Label(frame1,image=k).place(x=260,y=10,width=197,height=197)
	Label(frame1,text="Abhishek",font=("times new roman",30,"bold","italic","underline"),fg="black",bg="white").place(x=180,y=220)
	Label(frame1,text="Dhakad",font=("times new roman",30,"bold","italic","underline"),fg="black",bg="white").place(x=350,y=220)

	Label(frame1,text="I'm a second-year student \n pursuing Btech-CSE @LPU Punjab.",font=("Comic Sans MS",16,"italic"),fg="black",bg="white",justify="left").place(x=310,y=290)
	Label(frame1,text="I'm a self-learner and highly passionate\nto learn new Skills and Technologies.",font=("Comic Sans MS",16,"italic"),fg="black",bg="white",justify="left").place(x=310,y=360)

	Label(frame1,text="> Python Developer",font=("Comic sans MS",16,"bold"),fg="black",bg="white").place(x=10,y=290)
	Label(frame1,text="> Web Developer",font=("Comic sans MS",16,"bold"),fg="black",bg="white").place(x=10,y=340)
	Label(frame1,text="> Competitive Programmer",font=("Comic sans MS",16,"bold"),fg="black",bg="white",justify="left").place(x=10,y=390)

	Label(frame1,text="Contact me on",font=("Comic sans MS",20,"bold"),fg="black",bg="white",justify="left").place(x=240,y=440)
	
	instalogo=ImageTk.PhotoImage(file="images/instagram.png")
	maillogo=ImageTk.PhotoImage(file="images/mail.png")
	linkedinlogo=ImageTk.PhotoImage(file="images/linkedin.png")
	githublogo=ImageTk.PhotoImage(file="images/github.png")

	Button(frame1,image=instalogo,cursor="hand2",command=insta,bd=0).place(x=180,y=500,width=40,height=40)
	Button(frame1,image=maillogo,cursor="hand2",command=mail,bd=0).place(x=270,y=500,width=40,height=40)
	Button(frame1,image=linkedinlogo,cursor="hand2",command=linkedin,bd=0).place(x=360,y=500,width=40,height=40)
	Button(frame1,image=githublogo,cursor="hand2",command=github,bd=0).place(x=450,y=500,width=40,height=40)

	screen10.mainloop()

def insta():
	url="https://www.instagram.com/abhishek.dhakad_/"
	webbrowser.open(url)

def mail():
	url="mailto:abhishek.dhakad121@gmail.com"
	webbrowser.open(url)

def linkedin():
	url="https://www.linkedin.com/in/abhishek-dhakad-003740192"
	webbrowser.open(url)

def github():
	url = "https://github.com/AbhishekDhakad18"
	webbrowser.open(url)


def bot(browser,var1):
	global driver,username
	username = var1
	driver = browser
	global screen1
	screen1=Tk()
	screen1.resizable(False,False)
	screen1.title("InstaBot: Main Page")
	try:
		screen1.iconbitmap(r"images/icon.ico")
	except:
		pass

	global w,h
	w = screen1.winfo_screenwidth()
	h = screen1.winfo_screenheight()
	screen1.geometry(f"{w}x{h}+0+0")
	framex=Frame(screen1,bg="white",highlightthickness=3)
	framex.config(highlightbackground="gray")
	framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

	bg=ImageTk.PhotoImage(file="images/bg3.jpg")
	bg1=Label(framex,image=bg).place(relwidth=1,relheight=1)
	frame1=Frame(framex,bg="white",highlightthickness=2)
	frame1.config(highlightbackground="gray")
	frame1.place(x=500,y=100,width=300,height=530)

	Label(frame1, text = "Basic", fg = "black" ,font = ("bree serif",22,"bold"),bg="white").place(x=20,y=20,width=75,height=25)

	temp=Button(framex,text="DP",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=savedp).place(x=580,y=230,width=125,height=40)
	temp=Button(framex,text="Bio",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=savebio).place(x=580,y=390,width=125,height=40)
	temp=Button(framex,text="View",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=viewinfo).place(x=580,y=550,width=125,height=40)

	frame2=Frame(framex,bg="white",highlightthickness=2)
	frame2.config(highlightbackground="gray")
	frame2.place(x=850,y=100,width=450,height=530)

	Label(frame2, text = "Advance", fg = "black" ,font = ("bree serif",22,"bold"),bg="white").place(x=20,y=20,width=150,height=25)

	temp=Button(framex,text="Message",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=mssg).place(x=1110,y=210,width=125,height=40)
	temp=Button(framex,text="Bomber",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=bomb).place(x=890,y=300,width=125,height=40)
	temp=Button(framex,text="send-req",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=sendreq).place(x=1110,y=390,width=125,height=40)
	temp=Button(framex,text="followers",font=("calibri",14,"bold"),bg="violet",cursor="hand2",command=getlist).place(x=890,y=470,width=125,height=40)
	temp=Button(framex,text="Unfollow",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=unfollow).place(x=1110,y=550,width=125,height=40)
	temp=Button(framex,text="About Me",font=("calibri",16,"bold"),bg="navy",fg="yellow",cursor="hand2",command=contactme).place(x=1140,y=80,width=125,height=40)

	screen1.mainloop()