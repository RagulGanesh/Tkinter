from tkinter import *
from tkinter import messagebox
import re
root=Tk()
root.geometry("500x500")
root.configure(bg="#f79ec5")
def msg_userid():
    messagebox.showinfo('Error',"Enter valid Email Id")
def msg_password():
    messagebox.showinfo('Error',"Password should contain only alphanumeric characters")
def msg_register():
    messagebox.showinfo('Error',"First register to get logged in")
def msg_successreg():
    messagebox.showinfo('Success',"Successfully registered")
def msg_successlog():
    messagebox.showinfo('Success',"Successfully logged in")
def submit():
    get_username=userid_entry.get()
    get_password=password_entry.get()
    pattern1=r"[\w.-]+@[\w.-]+"
    pattern2=r"[\w]+"
    if re.match(pattern1,get_username)==None:
        msg_userid()
    if re.match(pattern2,get_password)==None:
        msg_password()
    if re.match(pattern1,get_username) and re.match(pattern2,get_password): 
        msg_successreg()  
        
    # messagebox.showinfo('Dialog Box',"Done")
        with open("AccountLogin.csv","a+") as file:
           file.write("{},{}".format(get_username,get_password))
           file.write("\n")
    print(get_username,get_password)
def submitFromLogin():
    global flag
    flag=0 
    pattern1=r"[\w.-]+@[\w.-]+"
    pattern2=r"[\w]+"
    get_username_login=userid_entry_from_login.get()
    get_password_login=password_entry_from_login.get()
    if re.match(pattern1,get_username_login)==None:
        msg_userid()
    if re.match(pattern2,get_password_login)==None:
        msg_password() 
    if re.match(pattern1,get_username_login) and re.match(pattern2,get_password_login):
        #msg_successlog()        
        with open("AccountLogin.csv","r+") as file:   
         
         for line in file:
            a=line.strip(",")
            print(a)
            #username=userid_entry.get()
            #password=password_entry.get()
            if get_username_login in a and get_password_login in a:
                message=Label(login_root,text="Account Login Successful")
                message.place(x=150,y=275)
                msg_successlog()
                print("Account Login Successful")
                flag=1
            #else:
                #continue
                #message=Label(login_root,text="Account Login UnSuccessful")
                #message.place(x=150,y=275)
                #print("Account Login UnSuccessful")
                #msg_register()
    if flag==0:
         msg_register()
    

def register():
    register_root=Tk()
    register_root.geometry("500x300")  
    register_root.title("Registration Form") 

    title = Label(register_root, text="Registration form",width=20,font=("Comic Sans MS", 20),fg="red")
    title.place(x=120,y=10) 

    userid_label=Label(register_root,text="UserID",font=("Comic Sans MS", 15))
    userid_label.place(x=25,y=80)
    
    password_label=Label(register_root,text="Password",font=("Comic Sans MS", 15))
    password_label.place(x=25,y=150)

    global userid_entry
    userid_entry=Entry(register_root)
    userid_entry.place(x=150,y=80,width=200,height=20)

    global password_entry
    password_entry=Entry(register_root,show='*')
    password_entry.place(x=150,y=150,width=200,height=20)

    #get_username=userid_entry.get()
    #get_password=password_entry.get()

    submit_button=Button(register_root,text="Submit",width=20,bg='brown',fg='white',padx=10,pady=10,command=submit)
    submit_button.place(x=125,y=220)

    register_root.mainloop()
def login():
    global login_root
    login_root=Tk()
    login_root.geometry("500x300")
    login_root.title("Account Login")
    #message=Label(login_root,text="Account Login Successful")
    #Label.pack()
    title_login = Label(login_root, text="Please enter your details to login",width=40,font=("Comic Sans MS", 15),fg="blue")
    title_login.place(x=30,y=10)

    enter_userid=Label(login_root,text="Username",font=("Comic Sans MS", 15),fg="red")
    enter_userid.place(x=200,y=60)

    enter_password=Label(login_root,text="Password",font=("Comic Sans MS", 15),fg="red")
    enter_password.place(x=200,y=130)

    global userid_entry_from_login
    userid_entry_from_login=Entry(login_root)
    userid_entry_from_login.place(x=150,y=100,width=200,height=20)

    global password_entry_from_login
    password_entry_from_login=Entry(login_root,show='*')
    password_entry_from_login.place(x=150,y=170,width=200,height=20)

    submit_button_login=Button(login_root,text="Login",width=10,bg='brown',fg='white',padx=5,pady=5,command=submitFromLogin)
    submit_button_login.place(x=200,y=210)

    login_root.mainloop()

    
    

    #login_root.mainloop()    
# global get_username
get_username=StringVar
# global get_password
get_password=StringVar
get_username_login=StringVar
get_password_login=StringVar
   
a=Label(text="Select your choice",bg="#9ef1f7",pady=50,font=("Comic Sans MS", 20,"underline"),fg="red")
a.pack(fill=X)
login_button=Button(text="Login",padx=100,pady=20,command=login,font=("Comic Sans MS", 15))
login_button.pack(pady=20)

register_button=Button(text="Register",padx=100,pady=20,command=register,font=("Comic Sans MS", 15))
register_button.pack(pady=20)

root.mainloop()
