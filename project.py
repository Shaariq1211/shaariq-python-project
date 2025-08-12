from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Registration")

root.geometry=("500x500")

l=Label(root,text="Name")
l.pack()
e1=Entry(root)
e1.pack()

m=Label(root,text="Age")
m.pack()
e2=Entry(root)
e2.pack()

n=Label(root,text="Place")
n.pack()
e3=Entry(root)
e3.pack()

o=Label(root,text="Email_id")
o.pack()
e4=Entry(root)
e4.pack()

p=Label(root,text="Password")
p.pack()
e5=Entry(root)
e5.pack()

def register():
    Name=e1.get()
    Age=e2.get()
    Place=e3.get()
    Email_id=e4.get()
    Password=e5.get()
    if Name=="shaariq" and Age=="21" and Place=="mayiladuthurai" and Email_id=="shaariq@gmail.com" and Password=="1234":
      print("You registered correctly")
    else:
        print("You are not registered")
        messagebox.showinfo("Error", "Please Enter Your Name , Age , place , Email_id and Password and give register")

b=Button(root,text="register", command=register)
b.pack()        
           
root.mainloop()