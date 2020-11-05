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
	title=Label( text = "New user?", fg = "green" ,font = ("times new roman",18,"bold"),bg="white").place(x=760,y=552,width=125,height=25)
	title=Label( text = "Already Member?", fg = "green" ,font = ("times new roman",18,"bold"),bg="white").place(x=900,y=552,width=220,height=25)
	btn=Button(text="Register",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=register_page).place(x=760,y=584,width=125,height=40)
	btn2=Button(text="Login",font=("calibri",16,"bold"),bg="violet",cursor="hand2",command=login).place(x=970,y=584,width=125,height=40)
	temp=Button(screen1,text="About Us",font=("calibri",16,"bold"),bg="violet",fg="black",cursor="hand2",command=aboutus).place(x=950,y=115,width=125,height=40)
	screen1.mainloop()

def login():
	screen1.destroy()
	login_page()

def register_page():
	screen1.destroy()
	import register

def login_page():
	global screen3
	screen3=Tk()
	screen3.resizable(False,False)
	screen3.title("InstaBot-Login")
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
			con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="instabot")
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
	Label(frame3,text="- Ethical Hacking,Python,\nWeb & Android Penetester ,\n Basic Linux",font=("times new roman",14),fg="black",bg="white").place(x=0,y=440)
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


main_page()