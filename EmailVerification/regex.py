# email verification in database 
# first create a file where password and username been stored
# Then ask the user,password
# Then check it is a valid email or not using regex
# Then if it is valid,check in the database ,create another window and close previous window.
# If it is invalid then intimate the user
# After opening a window,display the user details
import tkinter as tk
root=tk.Tk()
#root.resizable(False,False)
root.title('Email Verification')

class student():
	def __init__(name,rollno,sec,year,email):
		self.name=name
		self.rollno=rollno
		self.sec=sec
		self.year=year
		self.email=email
def show_password():
	pass
def login():
	fp=open(r'./student')
	x=fp.readlines()
	emails=[]
	passwords=[]
	for i in x:
		email,password,rollno,name,sec,year=i.split(',')
		emails.append(email)
		passwords.append(password)
		#print(email,password,rollno,name,sec,year[0:-1])
	fp.close()
	print(emails ,passwords)
	if username_input.get()!=None and password_input.get()!=None:
		#print(username_input.get(), password_input.get())
		if username_input.get() in emails and password_input.get() in passwords:
			ERROR.config(text='YOU LOGIN SUCCESSFULLY!')
			root.destroy()
			root2=tk.Tk()
			root2.title("STUDENT-DETAILS")
			root2.mainloop()
		else:
			ERROR.config(text='INVALID USERNAME OR PASSWORD',fg='red')
	else:
		ERROR.config(text='Enter username and password',fg='red')



username=tk.Label(root,text='username',width=15,fg='blue')
username_input=tk.Entry(root,width=30,fg='blue')
password=tk.Label(root,text='password',width=15,fg='black')
password_input=tk.Entry(root,show='*',width=30,fg='black')
LOGIN=tk.Button(root,padx=10,pady=6,fg='orange',bg='yellow',command=login,text='login')
ERROR=tk.Label(root,text='',width=30)
ERROR.grid(row=3,column=0)
LOGIN.grid(row=2,column=0)
username.grid(row=0,column=0)
username_input.grid(row=0,column=1)
password_input.grid(row=1,column=1)
password.grid(row=1,column=0)

root.mainloop()
