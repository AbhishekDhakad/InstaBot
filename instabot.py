from time import sleep
from tkinter import *
import tkinter as tk
from typing import Pattern
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
from tkinter import filedialog as fd
import itertools
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

btnstate = False

def savedp():
	global screen2
	screen2=Toplevel(screen1)
	screen2.resizable(False,False)
	screen2.title("InstaPy-Dpdownloader")
	try:
		screen2.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen2.geometry(f"{w}x{h}+0+0")
	screen2.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen2,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen2,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen2,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen2,text="Download Profile picture",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-740,y=70)
	Label(screen2,text="of multiple users",font=("Helvetica",22),bg="#1b3b5f",fg="#EDEDED").place(x=w-570,y=150)

	frame = Frame(screen2,bg="#455566")
	frame.place(x=w-750,y=240,width=600,height=500)

	
	global num1,dpusr


	Label(frame,text="Number of persons?",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=30)
	num1=ttk.Combobox(frame,font=("times new roman",18),state="readonly",justify=CENTER,background="#556080")
	num1['values']=("1","2","3","4","5","6","7","8","9","10")
	num1.place(x=150,y=100,width=300,height=30)
	num1.current(0)

	Label(frame,text="Usernames (seprated by space):",font=("calibri",22),bg="#455566",fg="#FFFFFF").place(x=20,y=200)

	dpusr=tk.Entry(frame,font=("times new roman",20),bg="#556080",fg="#FFFFFF")
	dpusr.place(x=150,y=270,width=300,height=40)

	btn = ImageTk.PhotoImage(file="images/downloadbtn.png")
	Button(frame,image=btn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_dp).place(x=150,y=400,width=300,height=70)

	screen2.state('zoomed')
	screen2.mainloop()

def verify_dp():
	if dpusr.get()=="" or num1.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen2)
	else:
		dpdownload()


def dpdownload():
	vic=dpusr.get().split()
	driver.set_window_size(800,820)
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
	screen3.title("InstaPy-Bio Saver")
	try:
		screen3.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen3.geometry(f"{w}x{h}+0+0")
	screen3.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen3,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen3,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen3,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen3,text="Save Bio in text file",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-680,y=70)
	Label(screen3,text="of multiple users",font=("Helvetica",22),bg="#1b3b5f",fg="#EDEDED").place(x=w-570,y=150)

	frame = Frame(screen3,bg="#455566")
	frame.place(x=w-750,y=240,width=600,height=500)
	

	global biousr,bionum

	Label(frame,text="Number of persons?",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=30)
	bionum=ttk.Combobox(frame,font=("times new roman",18),state="readonly",justify=CENTER,background="#556080")
	bionum['values']=("1","2","3","4","5","6","7","8","9","10")
	bionum.place(x=150,y=100,width=300,height=30)
	bionum.current(0)

	Label(frame,text="Usernames (seprated by space):",font=("calibri",22),bg="#455566",fg="#FFFFFF").place(x=20,y=200)

	biousr=tk.Entry(frame,font=("times new roman",20),bg="#556080",fg="#FFFFFF")
	biousr.place(x=150,y=270,width=300,height=40)

	btn = ImageTk.PhotoImage(file="images/savebtn.png")
	Button(frame,image=btn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_bio).place(x=150,y=400,width=300,height=70)

	screen3.state('zoomed')
	screen3.mainloop()

def verify_bio():
	if biousr.get()=="" or bionum.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen3)
	else:
		getbio()

def getbio():
	vic=biousr.get().split()
	driver.set_window_size(800,820)
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
	screen4.title("InstaPy-Get Others Details")
	try:
		screen4.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen4.geometry(f"{w}x{h}+0+0")
	screen4.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen4,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen4,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen4,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen4,text="Save User Info in text file",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-740,y=70)
	Label(screen4,text="of multiple users",font=("Helvetica",22),bg="#1b3b5f",fg="#EDEDED").place(x=w-580,y=150)
	

	global frameview

	frameview = Frame(screen4,bg="#455566")
	frameview.place(x=w-750,y=240,width=600,height=500)

	global viewusr
	
	Label(frameview,text="Usernames (seprated by space):",font=("calibri",22),bg="#455566",fg="#FFFFFF").place(x=40,y=40)

	viewusr=Entry(frameview,font=("times new roman",20),bg="#556080",fg="#FFFFFF")
	viewusr.place(x=150,y=100,width=300,height=45)

	Label(frameview,text="View result here:",font=("calibri",22),bg="#455566",fg="#FFFFFF").place(x=40,y=170)


	global viewlist
	scroll = Scrollbar(frameview,orient=VERTICAL)

	viewlist = Listbox(frameview,font=("times new roman",20),bg="#556080",fg="#FFFFFF",highlightthickness=0,borderwidth=0,yscrollcommand=scroll.set)
	scroll.config(command=viewlist.yview)
	viewlist.place(x=150,y=230,width=300,height=170)
	scroll.place(x=445,y=230,width=20,height=170)

	getbtn = ImageTk.PhotoImage(file="images/getbtn.png")
	Button(frameview,image=getbtn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_info).place(x=160,y=420)

	clearbtn = ImageTk.PhotoImage(file="images/clearbtn.png")
	Button(frameview,image=clearbtn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=clear_info).place(x=325,y=420)

	screen4.state('zoomed')
	screen4.mainloop()


def verify_info():
	if viewusr.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen4)
	else:
		getinfo()

def getinfo():
	vic=viewusr.get().split()
	driver.set_window_size(800,820)
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
	screen5.title("InstaPy-Send Message")
	try:
		screen5.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen5.geometry(f"{w}x{h}+0+0")
	screen5.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen5,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen5,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen5,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen5,text="Send Message",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-600,y=70)
	Label(screen5,text="to multiple users",font=("Helvetica",20),bg="#1b3b5f",fg="#EDEDED").place(x=w-530,y=150)

	frame = Frame(screen5,bg="#455566")
	frame.place(x=w-750,y=240,width=600,height=500)

	global usr1,msg1

	Label(frame,text="Usernames seprated by space: ",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=40)
	usr1=Entry(frame,font=("calibri",20),bg="#556080",fg="#FFFFFF")
	usr1.place(x=150,y=110,height=45,width=300)

	Label(frame,text="Your Message: ",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=220)
	msg1=Entry(frame,font=("calibri",20),bg="#556080",fg="#FFFFFF")
	msg1.place(x=150,y=290,width=300,height=45)

	btn = ImageTk.PhotoImage(file="images/sendbtn.png")
	Button(frame,image=btn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_msg).place(x=150,y=400,width=300,height=70)

	screen5.state('zoomed')
	screen5.mainloop()

def verify_msg():
	if usr1.get()=="" or msg1.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen5)
	else:
		msgsender()


def msgsender():
	message=msg1.get()
	victim=usr1.get().split()
	driver.set_window_size(800,820)
	for vic in victim:
		k=msg.sendmsg(driver,vic,message)
		if(k):
			screen5.destroy()
			print("Success - Message sent")
		else:
			print("Error - Invalid Username of Reciever ",k)
	driver.minimize_window()
	screen5.destroy()
	messagebox.showinfo("Success","Done")
	

################# bomber##########################

def bomb():
	global screen6
	screen6=Toplevel(screen1)
	screen6.resizable(False,False)
	screen6.title("InstaPy-Send Message")
	try:
		screen6.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen6.geometry(f"{w}x{h}+0+0")
	screen6.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen6,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen6,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen6,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen6,text="Send message to one user",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-750,y=70)
	Label(screen6,text="with many repitition",font=("Helvetica",20),bg="#1b3b5f",fg="#EDEDED").place(x=w-570,y=150)

	frame = Frame(screen6,bg="#455566")
	frame.place(x=w-750,y=240,width=600,height=500)

	global usr2,msg2,num2

	Label(frame,text="Their Username: ",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=20)
	usr2=Entry(frame,font=("calibri",20),bg="#556080",fg="#FFFFFF")
	usr2.place(x=160,y=80,height=45,width=300)

	Label(frame,text="Your Message: ",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=160)
	msg2=Entry(frame,font=("calibri",20),bg="#556080",fg="#FFFFFF")
	msg2.place(x=160,y=220,width=300,height=45)

	Label(frame,text="How many?: ",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=300)
	num2=Entry(frame,font=("calibri",20),bg="#556080",fg="#FFFFFF")
	num2.place(x=140,y=360,width=80,height=30)

	btn = ImageTk.PhotoImage(file="images/sendbtn.png")
	Button(frame,image=btn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_bomb).place(x=260,y=400,width=300,height=70)
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
	driver.set_window_size(800,820)
	
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
	screen7.title("InstaPy-Send Message")
	try:
		screen7.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen7.geometry(f"{w}x{h}+0+0")
	screen7.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen7,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen7,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen7,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen7,text="Send follow request",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-690,y=70)
	Label(screen7,text="to multiple users",font=("Helvetica",22),bg="#1b3b5f",fg="#EDEDED").place(x=w-570,y=150)

	frame = Frame(screen7,bg="#455566")
	frame.place(x=w-750,y=240,width=600,height=500)

	global num3,usr3

	Label(frame,text="Number of persons?",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=30)
	num3=ttk.Combobox(frame,font=("times new roman",18),state="readonly",justify=CENTER,background="#556080")
	num3['values']=("1","2","3","4","5","6","7","8","9","10")
	num3.place(x=150,y=100,width=300,height=30)
	num3.current(0)

	Label(frame,text="Usernames (seprated by space):",font=("calibri",22),bg="#455566",fg="#FFFFFF").place(x=20,y=200)

	usr3=tk.Entry(frame,font=("times new roman",20),bg="#556080",fg="#FFFFFF")
	usr3.place(x=150,y=270,width=300,height=40)

	btn = ImageTk.PhotoImage(file="images/followbtn.png")
	Button(frame,image=btn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_req).place(x=150,y=400,width=300,height=70)

	screen7.state('zoomed')
	screen7.mainloop()

def verify_req():
	if usr3.get()=="" or num3.get()=="":
		messagebox.showerror("Error","All Feild required",parent=screen6)
	else:
		req()

def req():
	victim=usr3.get().split()
	driver.set_window_size(800,820)
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
	screen8.title("InstaPy-Get follower/unfollower")
	try:
		screen8.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen8.geometry(f"{w}x{h}+0+0")
	screen8.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen8,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen8,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen8,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen8,text="Follower-Following-Unfollower",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-810,y=70)
	Label(screen8,text="in text file",font=("Helvetica",22),bg="#1b3b5f",fg="#EDEDED").place(x=w-510,y=150)

	global framelist

	framelist = Frame(screen8,bg="#455566")
	framelist.place(x=w-750,y=240,width=600,height=500)

	global usr4,password4,page4
	
	Label(framelist,text="Number of persons?",font=("calibri",24),bg="#455566",fg="#FFFFFF").place(x=20,y=20)
	page4=ttk.Combobox(framelist,font=("times new roman",18),state="readonly",justify=CENTER,background="#556080")
	page4['values']=("--select--","followers","following","unfollower")
	page4.place(x=150,y=80,width=300,height=40)
	page4.current(0)

	global mylist
	scroll = Scrollbar(framelist,orient=VERTICAL)

	mylist = Listbox(framelist,bg="#556080",font=("calibri",14),fg="#FFFFFF",yscrollcommand=scroll.set,highlightthickness=0,borderwidth=0)
	scroll.config(command=mylist.yview)
	mylist.place(x=120,y=180,width=350,height=200)
	scroll.place(x=465,y=180,width=20,height=200)

	btn1 = ImageTk.PhotoImage(file="images/getbtn.png")
	Button(framelist,image=btn1,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_localsave).place(x=150,y=410)
	
	global btnx
	btn2 = ImageTk.PhotoImage(file="images/save2btn.png")
	btnx = Button(framelist,image=btn2,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=savelist,state=DISABLED)
	btnx.place(x=320,y=410)

	screen8.state('zoomed')
	screen8.mainloop()

def verify_localsave():
	if page4.get()=="--select--":
		messagebox.showerror("Error","Select one",parent=screen8)
	else:
		localsave()

def localsave():
	page=page4.get()
	driver.set_window_size(800,820)
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

	btnx["state"] = NORMAL
	
	
	
def savelist():

	txt_file = fd.asksaveasfile(title="Save text file",filetypes=[("text file","*.txt")],defaultextension=[("text file","*.txt")],initialdir=os.getcwd(),mode='w')
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
	screen9.title("InstaPy-Unfollow Users")
	try:
		screen9.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen9.geometry(f"{w}x{h}+0+0")
	screen9.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen9,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen9,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen9,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)
	
	Label(screen9,text="Unfollow",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-550,y=70)
	Label(screen9,text="multiple users",font=("Helvetica",22),bg="#1b3b5f",fg="#EDEDED").place(x=w-540,y=150)

	global frametxt
	
	frametxt = Frame(screen9,bg="#455566")
	frametxt.place(x=w-750,y=240,width=600,height=500)

	Label(frametxt,text="Open text file containing Username list",font=("calibri",24),bg="#455566",fg="#FFFFFF").pack(pady=10)

	btn = ImageTk.PhotoImage(file="images/openbtn.png")
	Button(frametxt,image=btn,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=open_file).pack()
	
	Label(frametxt,text="- - - - - OR - - - - -",font=("calibri",28),bg="#455566",fg="#FFFFFF").pack()

	Label(frametxt,text="Write Usernames seprated by line",font=("calibri",24),bg="#455566",fg="#FFFFFF").pack()

	global text_box

	scroll = Scrollbar(frametxt,orient=VERTICAL)

	text_box = Text(frametxt,bg="#556080",font=("calibri",14),fg="#FFFFFF",highlightthickness=0,borderwidth=0,yscrollcommand=scroll.set)
	scroll.config(command=text_box.yview)
	text_box.place(x=150,y=240,width=300,height=160)
	scroll.place(x=445,y=240,width=20,height=160)

	btn2 = ImageTk.PhotoImage(file="images/unfollowbtn.png")
	Button(frametxt,image=btn2,bg="#455566",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=verify_unfollow).place(x=150,y=420)

	screen9.state('zoomed')
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
	driver.set_window_size(800,820)
	follow.unfollowacc(driver,lst)
	driver.minimize_window()
	messagebox.showinfo("Success","You did't follow them now",parent=screen9)


#--------------------------------------------about me---------------------------------------
def contactme():
	global screen10
	screen10=Toplevel(screen1)
	screen10.resizable(False,False)
	screen10.title("InstaPy-Contact Me")
	try:
		screen10.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen10.geometry(f"{w}x{h}+0+0")
	screen10.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen10,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen10,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen10,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)

	frame = Frame(screen10,bg="#455566")
	frame.place(x=w-850,y=150,width=700,height=600)

	me=ImageTk.PhotoImage(file="images/abhishek.png")
	Label(frame,image=me,bg="#455566").place(x=20,y=20)

	Label(frame,text="Abhishek Dhakad",font=("calibri",34),fg=fgfont,bg="#455566").place(x=270,y=50)
	Label(frame,text="●  I'm a second-year student pursuing\n    Btech-CSE.",font=("Poppin",18),fg=fgfont,bg="#455566",justify="left").place(x=225,y=150)
	Label(frame,text="●  I'm a self-learner and highly passionate\n    to learn new Skills and Technologies.",font=("Poppin",18),fg=fgfont,bg="#455566",justify="left").place(x=225,y=225)
	Label(frame,text="Skills",font=("calibri",28),fg=fgfont,bg="#455566").place(x=270,y=310)
	Label(frame,text="●  Python Developer",font=("Poppin",18),fg=fgfont,bg="#455566").place(x=225,y=380)
	Label(frame,text="●  Web Developer",font=("Poppin",18),fg=fgfont,bg="#455566").place(x=225,y=420)
	Label(frame,text="●  Competitive Programmer",font=("Poppins",18),fg=fgfont,bg="#455566",justify="left").place(x=225,y=460)
	
	githublogo=ImageTk.PhotoImage(file="images/github.png")
	instalogo=ImageTk.PhotoImage(file="images/instagram.png")
	linkedinlogo=ImageTk.PhotoImage(file="images/linkedin.png")

	Button(frame,image=githublogo,cursor="hand2",bg="#455566",command=github,activebackground="#455566",activeforeground="#FFFFFF",bd=0).place(x=20,y=530,width=40,height=40)
	Button(frame,image=linkedinlogo,cursor="hand2",bg="#455566",command=linkedin,activebackground="#455566",activeforeground="#FFFFFF",bd=0).place(x=100,y=530,width=40,height=40)
	Button(frame,image=instalogo,cursor="hand2",bg="#455566",command=insta,activebackground="#455566",activeforeground="#FFFFFF",bd=0).place(x=180,y=530,width=40,height=40)

	screen10.state('zoomed')
	screen10.mainloop()

def insta():
	url="https://www.instagram.com/abhishek.dhakad_/"
	webbrowser.open(url)

def linkedin():
	url="https://www.linkedin.com/in/abhishek-dhakad-003740192"
	webbrowser.open(url)

def github():
	url = "https://github.com/AbhishekDhakad18"
	webbrowser.open(url)

#---------------------------------------about instapy page-------------------------
def about_instapy():
	screen11=Toplevel(screen1)
	screen11.resizable(False,False)
	screen11.title("InstaPy-About InstaPy")
	try:
		screen11.iconbitmap(r"images/icon.ico")
	except:
		pass
	screen11.geometry(f"{w}x{h}+0+0")
	screen11.configure(bg="#1b3b5f")

	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen11,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen11,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen11,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)

	frame = Frame(screen11,bg="#455566")
	frame.place(x=w-850,y=150,width=700,height=600)

	Label(frame,text="InstaPy",font=("calibri",36),fg=fgfont,bg="#455566").place(x=20,y=10)
	Label(frame,text="An Instagram Bot",font=("calibri",28),fg=fgfont,bg="#455566").place(x=190,y=75)
	Label(frame,text="●  Instapy is an automation bot of instagram.",font=("Poppin",18),fg=fgfont,bg="#455566",justify="left").place(x=150,y=135)
	Label(frame,text="●  It has additional interesting and useful\n    features than instagram.",font=("Poppin",18),fg=fgfont,bg="#455566",justify="left").place(x=150,y=180)
	Label(frame,text="●  If you have any suggetion or request to \n    add any more feature do ping me on\n    instagram (given in about me).",font=("Poppin",18),fg=fgfont,bg="#455566",justify="left").place(x=150,y=255)

	Label(frame,text="Tech Used",font=("calibri",28),fg=fgfont,bg="#455566").place(x=190,y=360)
	Label(frame,text="●  Programming language - Python",font=("Poppin",18),fg=fgfont,bg="#455566").place(x=150,y=430)
	Label(frame,text="●  For GUI - Tkinter",font=("Poppin",18),fg=fgfont,bg="#455566").place(x=150,y=470)
	Label(frame,text="●  For automation - Selenium",font=("Poppins",18),fg=fgfont,bg="#455566",justify="left").place(x=150,y=510)
	Label(frame,text="●  For images design - Figma",font=("Poppins",18),fg=fgfont,bg="#455566",justify="left").place(x=150,y=550)

	screen11.state('zoomed')
	screen11.mainloop()

#---------------------------------------nav funtions-------------------------- 
def option_aboutme():
	navRoot.grab_release()
	contactme()

def option_about_instapy():
	navRoot.grab_release()
	about_instapy()

def option_logout():
	navRoot.grab_release()
	driver.quit()
	screen1.destroy()
	import home_page

def Exit():
	driver.quit()
	print("Application Closed")
	exit()

#-----------------------------------------fuction for nav switch---------------
def switch():
	global btnstate
	if btnstate is True:
		for x in range(1,303,3):
			navRoot.place(x=-x,y=0)
			navRoot.update()

		navRoot.grab_release()
		btnstate = False
	else:
		for x in range(-300,0,3):
			navRoot.place(x=x,y=0)
			navRoot.update()
		navRoot.grab_set()
		btnstate = True


def bot(browser,var1):
	global driver,username
	username = var1
	driver = browser
	global screen1
	screen1=Tk()
	screen1.resizable(False,False)
	screen1.title("InstaPy: Main Page")
	try:
		screen1.iconbitmap(r"images/icon.ico")
	except:
		pass

	global w,h
	w = screen1.winfo_screenwidth()
	h = screen1.winfo_screenheight()
	screen1.geometry(f"{w}x{h}+0+0")
	screen1.configure(bg="#1b3b5f")

	#robot and copyright
	robot = ImageTk.PhotoImage(file="images/robot.png")
	Label(screen1,image=robot,bg="#1b3b5f").place(x=80,y=(h-550)/2)
	copy = ImageTk.PhotoImage(file="images/copyright.png")
	Label(screen1,image=copy,bg="#1b3b5f").place(x=235,y=686,width=16,height=16)
	Label(screen1,text="2021 Abhishek Dhakad",font=("@Yu Gothic UI",12),bg="#1b3b5f",fg="#FFFFFF").place(x=255,y=680)

	#menu button
	# Frame(screen1,bg="#455566").place(x=0,y=50,width=70,height=1000)
	# Frame(screen1,bg="#6cffff").place(x=0,y=0,width=70,height=50)
	open_menu = ImageTk.PhotoImage(file="images/menu.png")
	Button(screen1,image=open_menu,bg="#1b3b5f",cursor="hand2",activebackground="#1b3b5f",highlightthickness=0,borderwidth=0,command=switch).place(x=15,y=3,width=45,height=45)


	#---------------------------------navwindow----------------
	global btnstate
	btnstate = FALSE

	global navRoot
	navRoot = tk.Frame(screen1, bg="#455566", height=1000, width=300)
	navRoot.place(x=-300, y=0)
	Frame(navRoot,bg="#6cffff",width=300,height=50).place(x=0, y=0)
	Label(navRoot,text="IntstaPy",font="Bahnschrift 18",bg="#6cffff",fg="black").place(x=30,y=10)

	close_menu = ImageTk.PhotoImage(file="images/menu.png")
	Button(navRoot,image=close_menu,bg="#6cffff",cursor="hand2",activebackground="#6cffff",highlightthickness=0,borderwidth=0,command=switch).place(x=250,y=3,height=45,width=45)
	
	#font for all option page background
	global fgfont
	fgfont = "#FFFFFF"

	#navbar buttons
	y = 90
	options = ["About Me", "About Instapy", "Logout", "Exit"]
	func = [option_aboutme, option_about_instapy, option_logout, Exit]
	for i in range(4):
		tk.Button(navRoot, text=options[i], font="BahnschriftLight 20", bg="#455566", fg="white", activebackground="#455566", activeforeground="#1b3b5f", bd=0,command=func[i]).place(x=25, y=y)
		y += 50


	#------------------------mainscreen--------------------
	Label(screen1,text="Hey, Instapy user \U0001F590",font=("@Yu Gothic UI",40),bg="#1b3b5f",fg="#FFFFFF").place(x=w-690,y=60)
	Label(screen1,text="Click the buttons",font=("Helvetica",22),bg="#1b3b5f",fg="#EDEDED").place(x=w-570,y=140)
	
	frame = Frame(screen1,bg="#455566")
	frame.place(x=w-750,y=240,width=600,height=500)
	
	Label(frame,text="Simple functions",font=("calibri",20),bg="#455566",fg="#FFFFFF").place(x=30,y=30)
	
	Button(frame,text="Dp",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=savedp).place(x=40,y=110,width=150,height=50)
	Button(frame,text="Bio",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=savebio).place(x=223,y=110,width=150,height=50)
	Button(frame,text="View User",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=viewinfo).place(x=405,y=110,width=150,height=50)
	
	Label(frame,text="Advance functions",font=("calibri",20),bg="#455566",fg="#FFFFFF").place(x=30,y=220)
	
	Button(frame,text="Message",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=mssg).place(x=40,y=300,width=150,height=50)
	Button(frame,text="Bomber",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=bomb).place(x=223,y=300,width=150,height=50)
	Button(frame,text="Follow",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=sendreq).place(x=405,y=300,width=150,height=50)
	
	Button(frame,text="Unfollowers",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=getlist).place(x=100,y=390,width=180,height=50)
	Button(frame,text="Unfollow",font=("calibri",25),bg="#c7cacf",cursor="hand2",activebackground="#455566",highlightthickness=0,borderwidth=0,command=unfollow).place(x=320,y=390,width=170,height=50)
		
	screen1.state('zoomed')
	screen1.mainloop()


if __name__ == "__main__":
    print("----------------------PLEASE RUN home_page.py--------")