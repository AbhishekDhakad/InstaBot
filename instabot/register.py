from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from instabot import bot
import mysql.connector


screen1=Tk()
screen1.resizable(False,False)
screen1.title("InstaBot-Register")
screen1.iconbitmap(r"images/icon.ico")

w = screen1.winfo_screenwidth()
h = screen1.winfo_screenheight()
screen1.geometry(f"{w}x{h}+0+0")

framex=Frame(screen1,bg="white",highlightthickness=3)
framex.config(highlightbackground="gray")
framex.place(x=(w-1350)/2,y=(h-700)//2-15,width=1350,height=700)

reg=ImageTk.PhotoImage(Image.open("images/Register_Page.jpg"))
reg1=Label(framex,image=reg).place(relwidth=1,relheight=1)
frame1=Frame(framex,bg="white")
frame1.place(x=560,y=80,width=700,height=550)

                              
title=Label(frame1,text="SIGN UP",font=("times new roman",35,"bold"),bg="white",fg="black").place(x=250,y=30)
f_name=Label(frame1,text="First Name:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=100)
txt_fname=Entry(frame1,font=("times new roman",15), bg="lightgrey")
txt_fname.place(x=50,y=130,width=250)
        
l_name=Label(frame1,text="Last Name:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=100)
txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
txt_lname.place(x=370,y=130,width=250)
       
        
email=Label(frame1,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=180)
txt_email1=Entry(frame1,font=("times new roman",15),bg="lightgrey")
txt_email1.place(x=370,y=210,width=250)
        
password=Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=270)
txt_password1=Entry(frame1,font=("times new roman",15),show="*",bg="lightgrey")
txt_password1.place(x=50,y=300,width=250)     
       
username=Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=180)
txt_username=Entry(frame1,font=("times new roman",15),bg="lightgrey")
txt_username.place(x=50,y=210,width=250)
var_chk=IntVar()
chk=Checkbutton(frame1,text="I Agree the Terms&Conditions",variable=var_chk,onvalue=1,offvalue=0,bg="white",fg="black",font=("times new roman",14)).place(x=50,y=380)
#label and entry for confirm password

cpassword=Label(frame1,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=270)
txt_cpassword1=Entry(frame1,font=("times new roman",15),show="*",bg="lightgrey")
txt_cpassword1.place(x=370,y=300,width=250)

def register():
        if txt_fname.get()=="" or txt_lname.get()=="" or txt_email1.get()=="" or txt_password1.get()=="" or txt_cpassword1.get()=="" or txt_username.get()=="" or var_chk.get()==0 :
            messagebox.showerror("ERROR","All Fields are Required",parent=screen1) 
            
        elif txt_password1.get()!=txt_cpassword1.get():
            messagebox.showerror("ERROR","Password and Confirm Password must be same",parent=screen1)
        
        else:
            con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="abhi")
            cursor=con.cursor()
            sql=("insert into login(username, password) values (%s,%s)")
            val=(txt_username.get(),txt_password1.get())
            cursor.execute(sql,val)
            con.commit()
            messagebox.showinfo("Register","Registered Successfully",parent=screen1)#connecting to database
            screen1.destroy()


btn_register=Button(frame1,bd=0,cursor="hand2",text="REGISTER",border=0,command=register, font=("times new roman",22),bg="green4", fg="black", width=16).place(x=230,y=450)

screen1.mainloop()

