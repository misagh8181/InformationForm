from tkinter import *
from tkinter import font
from tkinter import messagebox
from email import header
from operator import le
from turtle import color, right
from cProfile import label
from cgitb import text

def register(NameVar_name,NameVar_family,NameVar_id,NameVar_username1,NameVar_password1,NameVar_confirmpassword):
    if(NameVar_name.get()!="" and NameVar_family.get()!="" and NameVar_username1.get()!="" and NameVar_id.get()!="" and NameVar_password1.get()!="" and NameVar_confirmpassword.get()!=""):
        file=open("Informations.txt",mode="a")
        if(NameVar_password1.get()==NameVar_confirmpassword.get()):
            writting=True
            for line in open("Informations.txt"):
                data=eval(line)#Now we have a dictionary from our string by eval method wich was named data  
                if(NameVar_name.get()==data["name"] and NameVar_family.get()==data["familyname"] and NameVar_username1.get()==data["username"] and NameVar_id.get()==data["id"]and NameVar_password1.get()==data["password"]):
                    messagebox.showinfo("Exist","This user has been created :( !!!")
                    writting=False
            if(writting==True):
                file.write(str({"name":NameVar_name.get(),"familyname":NameVar_family.get(),"username":NameVar_username1.get(),"id":NameVar_id.get(),"password":NameVar_password1.get()})+"\n")
                NameVar_name.set("") 
                NameVar_family.set("")
                NameVar_username1.set("") 
                NameVar_id.set("") 
                NameVar_password1.set("")
                NameVar_confirmpassword.set("")
        else:
            messagebox.showerror("Error","The Password and Confirm Password arent the same !!!")
        file.close()
    else:
        messagebox.showerror("Error","Not all entries are given !!!")

def login(NameVar_username2,NameVar_password2):
    if(NameVar_username2.get()!="" and NameVar_password2.get()!=""):
        Exist=False
        for line in open("Informations.txt"):
            data=eval(line)#Now we have a dictionary from our string by eval method wich was named data  
            if(NameVar_username2.get()==data["username"]):
                if(NameVar_password2.get()==data["password"]):
                    messagebox.showinfo("Successful","success :)")
                    Exist=True
        if(Exist==False):
            messagebox.showinfo("Doesnt Exist","This user doesnt exist :( !!!")
            
    else:
        messagebox.showerror("Error","Not all entries are given!!!")

#region confige
root = Tk()
root.title("Information")
root.resizable(width=False,height=False)
root.geometry("600x500")
root.configure(bg="white")
#endregion confige

#region header
header=Frame(master=root,bg="blue")
header.pack(side=TOP,fill=X)
Label(master=header,text="Information",font=("arial",40,"bold"),bg="blue",fg="black").pack(side=TOP,fill=X)
#endregion header

#region right
right_frame=Frame(master=root,bg="brown")
right_frame.pack(side=RIGHT,fill=BOTH,expand=True)
right_frame.propagate(False)

Label(master=right_frame,bg="grey" ,fg="white", text="LOGIN",font=("arial",15,"bold")).pack(side=TOP,fill=X)

buttonFrame_right=Frame(master=right_frame,bg="maroon",height=40)
buttonFrame_right.pack(side=BOTTOM,fill=X)



body_username2=Frame(master=right_frame,bg="brown",height=40)
body_username2.pack(side=TOP,fill=X)
body_username2.propagate(False)
labelUserName2=Label(master=body_username2,text="UserName :",fg="black",bg="brown",font=("arial",10,"bold"))
labelUserName2.pack(side=TOP,anchor="w")
NameVar_username2=StringVar()
userNameEntry2=Entry(master=body_username2,textvariable=NameVar_username2,font=("arial",10,"normal"),width=35)
userNameEntry2.pack(side=BOTTOM)

body_password2=Frame(master=right_frame,bg="brown",height=40)
body_password2.pack(side=TOP,fill=X)
body_password2.propagate(False)
labelPassWord2=Label(master=body_password2,text="PassWord :",fg="black",bg="brown",font=("arial",10,"bold"))
labelPassWord2.pack(side=TOP,anchor="w")
NameVar_password2=StringVar()
passWordEntry2=Entry(master=body_password2,textvariable=NameVar_password2,font=("arial",10,"normal"),width=35)
passWordEntry2.pack(side=BOTTOM)

button1_right = Button(master=buttonFrame_right, text="Exit", bg="red", fg="white", width=7, height=2, command=root.destroy)
button1_right.pack(side=LEFT)

button2_right = Button(master=buttonFrame_right, text="login", bg="green", fg="white", width=7, height=2, command=lambda :login(NameVar_username2,NameVar_password2))
button2_right.pack(side=RIGHT)
#endregion right

#region center
center_frame=Frame(master=root,bg="black",width=2)
center_frame.pack(side=RIGHT,fill=Y)
center_frame.propagate(False)
#endregion center

#region left
left_frame=Frame(master=root,bg="brown")
left_frame.pack(side=LEFT,fill=BOTH,expand=True)
left_frame.propagate(False)

Label(master=left_frame,bg="grey" ,fg="white", text="REGISTER",font=("arial",15,"bold")).pack(side=TOP,fill=X)

buttonFrame_left=Frame(master=left_frame,bg="maroon",height=40)
buttonFrame_left.pack(side=BOTTOM,fill=X)

body_name=Frame(master=left_frame,bg="brown",height=40)
body_name.pack(side=TOP,fill=X)
body_name.propagate(False)
labelName=Label(master=body_name,text="Name :",fg="black",bg="brown",font=("arial",10,"bold"))
labelName.pack(side=TOP,anchor="w")
NameVar_name=StringVar()
nameEntry=Entry(master=body_name,textvariable=NameVar_name,font=("arial",10,"normal"),width=35)
nameEntry.pack(side=BOTTOM)

body_familyname=Frame(master=left_frame,bg="brown",height=40)
body_familyname.pack(side=TOP,fill=X)
body_familyname.propagate(False)
labeFamilyName=Label(master=body_familyname,text="Family Name :",fg="black",bg="brown",font=("arial",10,"bold"))
labeFamilyName.pack(side=TOP,anchor="w")
NameVar_family=StringVar()
familyNameEntry=Entry(master=body_familyname,textvariable=NameVar_family,font=("arial",10,"normal"),width=35)
familyNameEntry.pack(side=BOTTOM)

body_username1=Frame(master=left_frame,bg="brown",height=40)
body_username1.pack(side=TOP,fill=X)
body_username1.propagate(False)
labelUserName=Label(master=body_username1,text="UserName :",fg="black",bg="brown",font=("arial",10,"bold"))
labelUserName.pack(side=TOP,anchor="w")
NameVar_username1=StringVar()
userNameEntry1=Entry(master=body_username1,textvariable=NameVar_username1,font=("arial",10,"normal"),width=35)
userNameEntry1.pack(side=BOTTOM)

body_id=Frame(master=left_frame,bg="brown",height=40)
body_id.pack(side=TOP,fill=X)
body_id.propagate(False)
labelId=Label(master=body_id,text="Id :",fg="black",bg="brown",font=("arial",10,"bold"))
labelId.pack(side=TOP,anchor="w")
NameVar_id=StringVar()
idEntry=Entry(master=body_id,textvariable=NameVar_id,font=("arial",10,"normal"),width=35)
idEntry.pack(side=BOTTOM)

body_password1=Frame(master=left_frame,bg="brown",height=40)
body_password1.pack(side=TOP,fill=X)
body_password1.propagate(False)
labelPassWord1=Label(master=body_password1,text="PassWord :",fg="black",bg="brown",font=("arial",10,"bold"))
labelPassWord1.pack(side=TOP,anchor="w")
NameVar_password1=StringVar()
passWordEntry1=Entry(master=body_password1,textvariable=NameVar_password1,font=("arial",10,"normal"),width=35)
passWordEntry1.pack(side=BOTTOM)

body_confirmpassword=Frame(master=left_frame,bg="brown",height=40)
body_confirmpassword.pack(side=TOP,fill=X)
body_confirmpassword.propagate(False)
labelConfirmPassWord=Label(master=body_confirmpassword,text="Confirm PassWord :",fg="black",bg="brown",font=("arial",10,"bold"))
labelConfirmPassWord.pack(side=TOP,anchor="w")
NameVar_confirmpassword=StringVar()
passWordEntry=Entry(master=body_confirmpassword,textvariable=NameVar_confirmpassword,font=("arial",10,"normal"),width=35)
passWordEntry.pack(side=BOTTOM)

button1_left = Button(master=buttonFrame_left, text="Exit", bg="red", fg="white", width=7, height=2, command=root.destroy)
button1_left.pack(side=LEFT)

button2_left = Button(master=buttonFrame_left, text="register", bg="green", fg="white", width=7, height=2, command=lambda :register(NameVar_name,NameVar_family,NameVar_id,NameVar_username1,NameVar_password1,NameVar_confirmpassword))
button2_left.pack(side=RIGHT)
#endregion left

root.mainloop()