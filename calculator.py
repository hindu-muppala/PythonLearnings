import tkinter as tk
from functools import partial
list2=[]
list3=[]
list1=[]
string=None
import re
base=tk.Tk()
base.title('MY FIRST CALCULATOR')
god=tk.Button(base,text='0',padx=30,pady=10)
def operator1(v):
	global string,list2
	list2.append(v)
	string=''.join(list2)
	god.config(text=string)
def packc(botto,x,y):
	botto.grid(row=x,column=y)
def converting(string):
	global list1
	list1=re.findall('\d+',string)
def operator_button(v):
	global string,list2,list3
	list2.append(v)
	string=''.join(list2)
	list3.append(v)
	god.config(text=string)
def null():
	global string,list2,list3
	string=[]
	list2=[]
	list3=[]
	global_value=0
	god.config(text='')
def total_value():
	global god,string,list2,list3
	converting(string)
	for d in range(len(list3)):
		if '%' in list3:
			x=list3.index('%')
			globalvalue2=float(list1[x])/float(list1[x+1])
			list1.pop(x+1)
			list1.pop(x)
			list3.pop(x)
			list1.insert(x,str(globalvalue2))
			
		if '*' in list3:
			x=list3.index('*')
			globalvalue2=float(list1[x+1])*float(list1[x])
			list1.pop(x+1)
			list1.pop(x)
			list3.pop(x)
			list1.insert(x,str(globalvalue2))

		if '+' in list3:
			x=list3.index('+')
			globalvalue2=float(list1[x+1])+float(list1[x])
			list1.pop(x+1)
			list1.pop(x)
			list3.pop(x)
			list1.insert(x,str(globalvalue2))
		if '-' in list3:
			x=list3.index('-')
			globalvalue2=float(list1[x])-float(list1[x+1])
			list1.pop(x+1)
			list1.pop(x)
			list3.pop(x)
			list1.insert(x,str(globalvalue2))
	string=str(int(float(list1[0])))
	list2=string.split()
	print(string ,list1 ,list2 ,list3 )
	god.config(text=list1[0])
one=tk.Button(base,text='1',padx=10,pady=10,command=partial(operator1,'1'))
two=tk.Button(base,text='2',padx=10,pady=10,command=partial(operator1,'2'))
three=tk.Button(base,text='3',padx=10,pady=10,command=partial(operator1,'3'))
four=tk.Button(base,text='4',padx=10,pady=10,command=partial(operator1,'4'))
five=tk.Button(base,text='5',padx=10,pady=10,command=partial(operator1,'5'))
six=tk.Button(base,text='6',padx=10,pady=10,command=partial(operator1,'6'))
seven=tk.Button(base,text='7',padx=10,pady=10,command=partial(operator1,'7'))
eight=tk.Button(base,text='8',padx=10,pady=10,command=partial(operator1,'8'))
nine=tk.Button(base,text='9',padx=10,pady=10,command=partial(operator1,'9'))
zero=tk.Button(base,text='0',padx=10,pady=10,command=partial(operator1,'0'))
plus=tk.Button(base,text='+',padx=10,pady=10,command=partial(operator_button,'+'))
minus=tk.Button(base,text='-',padx=10,pady=10,command=partial(operator_button,'-'))
multi=tk.Button(base,text='*',padx=10,pady=10,command=partial(operator_button,'*'))
divide=tk.Button(base,text='%',padx=10,pady=10,command=partial(operator_button,'%'))
clear=tk.Button(base,text='C',padx=10,pady=10,command=null)
totalvalue=tk.Button(base,text='=',padx=10,pady=10,command=total_value)
packc(seven,3,0)
packc(eight,3,1)
packc(nine,3,2)
packc(four,4,0)
packc(five,4,1)
packc(six,4,2)
packc(one,5,0)
packc(two,5,1)
packc(three,5,2)
packc(zero,6,1)
packc(plus,3,3)
packc(minus,4,3)
packc(multi,5,3)
packc(divide,6,3)
god.grid(row=2,column=0,columnspan=4)
packc(clear,6,0)
packc(totalvalue,6,2)
base.mainloop()
