from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from instabot import bot
import mysql.connector


def main_page():
	global screen1
	screen1=Tk()
	screen1.resizable(False,False)
	screen1.title("InstaBot")
	screen1.iconbitmap(r"images/icon.ico")
	screen1.geometry("1350x700+25+100")
	bg=ImageTk.PhotoImage(file="images/Main_Page.jpg")
	bg1=Label(screen1,image=bg).place(relwidth=1,relheight=1)
	title=Label( text = "New user?", fg = "navy" ,font = ("times new roman",18,"bold"),bg="white").place(x=760,y=560,width=125,height=25)
	title=Label( text = "Already Member?", fg = "navy" ,font = ("times new roman",18,"bold"),bg="white").place(x=905,y=560,width=220,height=25)
	btn=Button(text="Register",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=register_page).place(x=770,y=593,width=125,height=40)
	btn2=Button(text="Login",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=login).place(x=970,y=593,width=125,height=40)
	screen1.mainloop()

def login():
	screen1.destroy()
	login_page()

def register_page():
	screen1.destroy()
	import register
	login_page()

def login_page():
	global screen3
	screen3=Tk()
	screen3.resizable(False,False)
	screen3.title("InstaBot-Login")
	screen3.iconbitmap(r"images/icon.ico")
	screen3.geometry("1350x700+25+100")
	reg=ImageTk.PhotoImage(file="images/Login_Page.jpg")
	reg1=Label(screen3,image=reg).place(relwidth=1,relheight=1)

	global usr,pwd
	usr=Entry(font=("times new roman",15),bg="lightgray")
	usr.place(x=745,y=310,width=390,height=35)

	pwd=Entry(font=("times new roman",15),show="*",bg="lightgray")
	pwd.place(x=745,y=410,width=390,height=35)

	btn3=Button(text="Login",font=("calibri",16,"bold"),bg="SlateBlue2",cursor="hand2",command=verify_login).place(x=875,y=515,width=125,height=40)
	screen3.mainloop()

def verify_login():
	if usr.get()=="" or pwd.get()=="":
		messagebox.showerror("Error","All Field required",parent=screen3)
	else:
		try:
			con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="abhi")
			cur=con.cursor()
			cur.execute("select * from login where username=%s and password=%s",(usr.get(),pwd.get()))
			chk=cur.fetchone()
			if chk==None:
				messagebox.showerror("Error","Invalid Username & Password",parent=screen3)
			else:
				messagebox.showinfo("Success","Welcome",parent=screen3)
				activate_bot()

		except Exception as es:
			messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=screen3)


def activate_bot():
	screen3.destroy()
	bot()


main_page()