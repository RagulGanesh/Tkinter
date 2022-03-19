from tkinter import*
import re
from tkinter import messagebox
def msg_num():
    messagebox.showinfo("Error","Enter 10 digit phone number")  
def msg_email():
    messagebox.showinfo("Error","Enter correct email address") 
def msg_chkbtn():
    messagebox.showinfo("Error","Check the terms and conditions")
#def msg_caps():
    #messagebox.showinfo("Error","Only Uppercase applicable")
def msg_exists():
    messagebox.showinfo("Error","User already exists")    
def submit():
    get_fn=fname_entry.get()
    get_em=email_entry.get()
    get_age=age.get()    
    get_number=number.get()
    b=get_gender.get()
    pattern1=r"\d{10}\b" 
    pattern2=r"[\w.-]+@[\w.-]+"
    #if get_fn.islower():
        #msg_caps()     
    if re.match(pattern1,get_number)==None:
        msg_num()
    if re.match(pattern2,get_em)==None:
        msg_email()
    if get_chkbtn.get()==0:
        msg_chkbtn()     
    if b==1:
        put="Male"
    else:
        put="Female" 
    #with open("StudentRegistrationForm.txt","a") as f:
        #f.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number)) 
        #f.write("\n")              
    #if re.match(pattern1,get_number) and re.match(pattern2,get_em) and get_chkbtn.get()==1:
        #print(get_fn,get_em,get_age,put,get_number)
        # with open("StudentRegistrationForm.txt","a") as f:
        #     f.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number)) 
        #     f.write("\n")  
        #file=open("StudentRegistrationForm.csv","a")
        #file.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number))
        #file.write("\n")
        #file.close()
    flag=0    
    if re.match(pattern1,get_number) and re.match(pattern2,get_em) and get_chkbtn.get()==1:
        with open("StudentRegistrationForm.csv","r") as file:
            for line in file:
                k=line.strip(",")
                print(k)
                if get_fn in k and get_em in k and get_age in k and get_number in k:
                    msg_exists()
                    flag=1

        if flag==0:
           with open("StudentRegistrationForm.csv","a+") as f:
                    f.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number))
                    f.write("\n")
                    print(get_fn,get_em,get_age,put,get_number)            
                   

         
     
root = Tk()
get_fn=StringVar
get_em=StringVar
get_gender=IntVar()
get_age=StringVar
get_number=StringVar
get_chkbtn=IntVar()
root.geometry('500x500')
root.title("Registration Form")

title = Label(root, text="Registration form",width=20,font=("Comic Sans MS",20,"underline"),fg="red",)
title.place(x=90,y=53)

fullname = Label(root, text="FullName",width=20,font=("Comic Sans MS",15))
fullname.place(x=35,y=130)

fname_entry = Entry(root)
fname_entry.place(x=240,y=135)

email = Label(root, text="Email",width=20,font=("Comic Sans MS",15))
email.place(x=18,y=180)

email_entry = Entry(root)
email_entry.place(x=240,y=190)

gender = Label(root, text="Gender",width=20,font=("Comic Sans MS",15))
gender.place(x=28,y=230)

# var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=get_gender, value=1,font=("Comic Sans MS",15)).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=get_gender, value=2,font=("Comic Sans MS",15)).place(x=320,y=230)

age= Label(root, text="Age",width=20,font=("Comic Sans MS",15))
age.place(x=10,y=280)

age= Entry(root)
age.place(x=240,y=290)


number = Label(root, text="Mobile No.",width=20,font=("Comic Sans MS",15))
number.place(x=40,y=320)

number= Entry(root)
number.place(x=240,y=330)

sub=Button(root, text='Submit',width=20,bg='brown',fg='white',command=submit,font=("Comic Sans MS",10)).place(x=180,y=440)

get_chkbtn=IntVar()
Checkbutton(root, text="Terms and Condition", variable=get_chkbtn,font=("Comic Sans MS",15)).place(x=150,y=375)
root.mainloop()
