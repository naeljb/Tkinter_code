# importing the necessary libraries for my codes 
from tkinter import *
from tkinter import messagebox,filedialog, ttk
import math
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#____________________________________________________________________________
# creating my main window

root = Tk()
root.title("Nael's PBS App")
root.geometry("800x400")
root.iconbitmap("c:/guis/logo.ico")
#____________________________________________________________________________

# Creating my total function into my total frame

def total ():
	
	# Hiding all frames execpt total frame  
	hide_frame()
	total_frame.pack(fill="both",expand=1)

	# creating sample size initial function 
	
	def ss_initial():	
		# calculating  square of marging  of error 
		moesquare = DoubleVar()
		moesquare = pow((int(target.get())*0.1),2)

		# Calculating square of standar deviation 	  
		standar = IntVar()
		standar= int(MAX.get()) - int(MIN.get())
	
		standarsquare = DoubleVar
		standarsquare = float(pow((standar/6),2))

		#calculating the square of population
		popsquare = IntVar
		popsquare = pow(int(N.get()),2)

		# Calculating  initial sample size 
		global s1
		s1 = IntVar()
		s1 = math.ceil((popsquare*3.8416*standarsquare)/moesquare)
	
		# putting the calculaiton response on the screen for initial sample size 
		response_label.config(text="  The initial sample size is : " + str(s1),font=("helvetica",10))

	# Creating function for adjustments 

	def adjustment():
	
		# creating the checking variable and  adjustment 1
		a = DoubleVar()
		a = float(N.get())* 0.05

		z = DoubleVar()
		z = s1 / int(N.get())


		global ajd1
		ajd1 = DoubleVar()

		if s1 < a:
			ajd1 =1

		else:
			ajd1 = 1 /(1+ z)

		# creation of non-response adjustment 
		global ajd2
		ajd2 = DoubleVar()
		ajd2.set('0.00')
		b = DoubleVar
		b = int(nr.get()) /100
		ajd2 = 1 + b

		# Calculating  final  sample size 
		global s2
		s2 = DoubleVar()
		s2 = math.floor(s1 * ajd1 * float(d.get()) * ajd2)
	
		# putting the calculaiton response on the screen for final sample size 
		response_label1.config(text="  The sample size after ajustments is : " + str(s2),font=("helvetica",10))

		# creating my condition for minimun requiered 
		global x
		x = DoubleVar

		if s2 < 339:
			x =339
		
		else:
			x = ""

		response_label2.config(text= str(x) + "  as a minimum is recommended" )

	# Creating my reset_entry function 
	def reset_entry():
		N.delete(0,'end')
		MAX.delete(0,'end')
		MIN.delete(0,'end')
		d.delete(0,'end')
		nr.delete(0,'end')
		target.delete(0,'end')
	 
    # Creating a message for total of beneficiaries 
	N_message = Label(total_frame,text= "Total number of beneficiaries reached")
	N_message.grid(row=1, column=1,sticky = W,pady=5,padx=5)

	#Creating entry box total of beneficiaries
	N = Entry(total_frame)
	N.grid(row=1, column=2,pady=5)

	# Creating a message for the maximum value for a beneficiary 
	MAX_message = Label(total_frame,text= "Indicator maximum value for a beneficiary (set it 3 if unknow)")
	MAX_message.grid(row=2, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for the maximum value for a beneficiary 
	MAX = Entry(total_frame)
	MAX.grid(row=2, column=2,pady=5) 

	# Creating a message for the minimum value for a beneficiary 
	MIN_message = Label(total_frame,text= "Inidicator minimum value for a beneficiary,(set it 0 if unknow)")
	MIN_message.grid(row=3, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for the minimum  value for a beneficiary 
	MIN = Entry(total_frame)
	MIN.grid(row=3, column=2,pady=5)

	# Creating a message for design effect adjustment  
	design_effect = Label(total_frame,text= "Design effect (2 for two stages cluster with no prior information)")
	design_effect.grid(row=6, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for design effect  
	d = Entry(total_frame)
	d.grid(row=6, column=2,pady=5)

	# Creating a message for non-response rate  
	non_response_message = Label(total_frame,text= "Expected non-response rate (5%  if not known)")
	non_response_message.grid(row=5, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for non response rate  
	nr = Entry(total_frame)
	nr.grid(row=5, column=2,pady=5)

	# Creating a message for the target value of indicator 
	target_message = Label(total_frame,text= "Indicator target expressed as a total for the entire beneficiaries")
	target_message.grid(row=4, column=1,sticky = W,pady=5,padx=5) 

	# Creating entry box for the target value of indicator  
	target = Entry(total_frame)
	target.grid(row=4, column=2,pady=5)

	# Creating a button for calculating initial sample size 
	calculate_button1 = Button(total_frame,text="Calculate initial Sample Size", command= ss_initial)
	calculate_button1.grid(row=7, column=1,pady=10)

	# Creating a button for calculating final sample size 
	calculate_button1 = Button(total_frame,text="Calculate final Sample Size", command= adjustment)
	calculate_button1.grid(row=8, column=1,pady=10)

	#  Creating a response button for the first sample size 
	response_label=Label(total_frame,text="", pady=10)
	response_label.grid(row=7, column=2,pady=10)

	# Creating a response button for the final  sample size 
	response_label1=Label(total_frame,text="", pady=10)
	response_label1.grid(row=8, column=2,pady=10)

	# Creating a response button for mininum sample recommended 
	response_label2=Label(total_frame,text="")
	response_label2.grid(row=9, column=2,pady=5)

	# Creating my clear and reset entry button 
	reset = Button(total_frame,text='Clear & reset all entries', command=reset_entry)
	reset.grid(row=10, column=1,pady=10)
	
#____________________________________________________________________________
# Creating my mean function
def mean ():
	hide_frame()
	mean_frame.pack(fill="both",expand=1)

	def ss_initial():
		
		# Calculating square of standar deviation 	  
		standar = IntVar()
		standar= int(MAX.get()) - int(MIN.get())
	
		standarsquare = DoubleVar
		standarsquare = float(pow((standar/6),2))

		# calculating  square of marging  of error 
		moesquare = DoubleVar()
		error_decimal = float(error.get()) /100
		moesquare = pow((float(target.get())*error_decimal),2)

		# Calculating  initial sample size 
		global s1
		s1 = IntVar()
		s1 = math.ceil((3.8416*standarsquare)/moesquare)
	
		# putting the calculaiton response on the screen for initial sample size 
		response_label.config(text="  The initial sample size is : " + str(s1),font=("helvetica",10))

	# Creating function for adjustments 

	def adjustment():
		
		# creating the checking variable and  adjustment 1
		a = DoubleVar
		a = float(N.get())* 0.05

		global ajd1
		ajd1 = DoubleVar

		if s1 < a:
			ajd1 =1

		else:
			ajd1 = 0.5

		# creation of non-response adjustment 
		global ajd2
		ajd2 = DoubleVar
		b = DoubleVar
		b = int(nr.get()) /100
		ajd2 = 1 + b

		# Calculating  final  sample size 
		global s2
		s2 = DoubleVar()
		s2 = math.ceil(s1 * ajd1 * float(d.get()) * ajd2)
	
		# putting the calculaiton response on the screen for final sample size 
		response_label1.config(text="  The final sample size after ajustment is : " + str(s2),font=("helvetica",10))

		# creating my condition for minimun requiered 
		global x
		x = DoubleVar

		if s2 < 339:
			x =339
		
		else:
			x = ""

		response_label2.config(text= str(x) + "  as a minimum is recommended" )

	# Creating my reset_entry function 
	def reset_entry():
		N.delete(0,'end')
		MAX.delete(0,'end')
		MIN.delete(0,'end')
		d.delete(0,'end')
		nr.delete(0,'end')
		target.delete(0,'end')
		error.delete(0,'end')

	# Creating a message for the maximum value for a beneficiary 
	MAX_message = Label(mean_frame,text= "Expected  indicator maximum value for a beneficiary")
	MAX_message.grid(row=1, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for the maximum value for a beneficiary 
	MAX = Entry(mean_frame)
	MAX.grid(row=1, column=2,pady=5) 

	# Creating a message for the minimum value for a beneficiary 
	MIN_message = Label(mean_frame,text= "Expected inidicator minimum value for a beneficiary")
	MIN_message.grid(row=2, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for the minimum  value for a beneficiary 
	MIN = Entry(mean_frame)
	MIN.grid(row=2, column=2,pady=5)

	# Creating a message for the target value of indicator 
	target_message = Label(mean_frame,text= "Indicator target expressed as a mean")
	target_message.grid(row=3, column=1,sticky = W,pady=5,padx=5) 

	# Creating entry box for the target value of indicator  
	target = Entry(mean_frame)
	target.grid(row=3, column=2,pady=5)

	# Creating a message for the percentage error  
	error_message = Label(mean_frame,text= "Percentage error (5-10%, recommended 10%  for annual monitoring) ")
	error_message.grid(row=4, column=1,sticky = W,pady=5,padx=5) 

	# Creating entry box for the target value of indicator  
	error = Entry(mean_frame)
	error.grid(row=4, column=2,pady=5)

	# Creating a message for total of beneficiaries 
	N_message = Label(mean_frame,text= "Number of beneficiaries reached (needed for adjustment)")
	N_message.grid(row=5, column=1,sticky = W,pady=5,padx=5)

	#Creating entry box total of beneficiaries
	N = Entry(mean_frame)
	N.grid(row=5, column=2,pady=5)

	# Creating a message for non-response rate  
	non_response_message = Label(mean_frame,text= "Expected non-response rate (needed for adjustment and 5%  if not known)")
	non_response_message.grid(row=6, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for non response rate  
	nr = Entry(mean_frame)
	nr.grid(row=6, column=2,pady=5)

	# Creating a message for design effect adjustment  
	design_effect = Label(mean_frame,text= "Design effect (needed for adjustment, 2 for two stages cluster with no prior information)")
	design_effect.grid(row=7, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for design effect  
	d = Entry(mean_frame)
	d.grid(row=7, column=2,pady=5)

	# Creating a button for calculating initial sample size 
	calculate_button1 = Button(mean_frame,text="Calculate initial Sample Size", command= ss_initial)
	calculate_button1.grid(row=8, column=1,pady=10)

	# Creating a button for calculating final sample size 
	calculate_button1 = Button(mean_frame,text="Calculate final Sample Size", command= adjustment)
	calculate_button1.grid(row=9, column=1,pady=10)

	#  Creating a response button for the first sample size 
	response_label=Label(mean_frame,text="", pady=10)
	response_label.grid(row=8, column=2,pady=10)

	# Creating a response button for the final  sample size 
	response_label1=Label(mean_frame,text="", )
	response_label1.grid(row=9, column=2,pady=10)

	# Creating a response button for mininum sample recommended 
	response_label2=Label(mean_frame,text="")
	response_label2.grid(row=10, column=2,pady=5)

	# Creating my clear and reset entry button 
	reset = Button(mean_frame,text='Clear & reset all entries', command=reset_entry)
	reset.grid(row=11, column=1,pady=11)
#____________________________________________________________________________
# Creating my proportion function
def proportion ():
	hide_frame()
	proportion_frame.pack(fill="both",expand=1)

	def ss_initial():
		
		# calculating p*(1-p)
		p_decimal = DoubleVar
		p_decimal = float(p.get()) / 100
		
		a = DoubleVar
		a = 1 - p_decimal
		
		b = DoubleVar
		b = p_decimal * a

		# calculation error square

		# calculating  square of marging  of error 
		moesquare = DoubleVar()
		error_decimal = float(error.get()) /100
		moesquare = pow(error_decimal,2)

		# Calculating  initial sample size 
		global s1
		s1 = IntVar()
		s1 = math.ceil((3.8416*b)/moesquare)
	
		# putting the calculaiton response on the screen for initial sample size 
		response_label.config(text="  The initial sample size is : " + str(s1),font=("helvetica",10))

	def adjustment():
		
		# creating the checking variable and  adjustment 1
		c = DoubleVar
		c = float(N.get())* 0.05

		global ajd1
		ajd1 = DoubleVar

		if s1 < c:
			ajd1 =1

		else:
			ajd1 = 0.5

		# creation of non-response adjustment 
		global ajd2
		ajd2 = DoubleVar
		d = DoubleVar
		d = int(nr.get()) /100
		ajd2 = 1 + b

		# Calculating  final  sample size 
		global s2
		s2 = DoubleVar()
		s2 = math.ceil(s1 * ajd1 * float(d_effect.get()) * ajd2)
	
		# putting the calculaiton response on the screen for final sample size 
		response_label1.config(text="  The final sample size after ajustment is : " + str(s2),font=("helvetica",10))


		# creating my condition for minimun requiered 
		global x
		x = DoubleVar

		if s2 < 339:
			x =339
		
		else:
			x = ""

		response_label2.config(text=  str(x) + "  as a minimum is recommended" )

	# Creating my reset_entry function 
	def reset_entry():
		p.delete(0,'end')
		error.delete(0,'end')
		N.delete(0,'end')
		nr.delete(0,'end')
		d_effect.delete(0,'end')

	# Creating a message for proportion  
	p_message = Label(proportion_frame,text= " Estimate of proportion from prior survey")
	p_message.grid(row=1, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for proportion 
	p = Entry(proportion_frame)
	p.grid(row=1, column=2,pady=5) 

	# Creating a message for percentage of error  
	error_message = Label(proportion_frame,text= "Percentage error (5-10%, recommended 10%  for annual monitoring) ")
	error_message.grid(row=2, column=1,sticky = W,pady=5,padx=5) 

	# Creating entry box for the target value of indicator  
	error = Entry(proportion_frame)
	error.grid(row=2, column=2,pady=5)

	# Creating a message for total of beneficiaries 
	N_message = Label(proportion_frame,text= "Number of beneficiaries reached (needed for adjustment)")
	N_message.grid(row=3, column=1,sticky = W,pady=5,padx=5)

	#Creating entry box total of beneficiaries
	N = Entry(proportion_frame)
	N.grid(row=3, column=2,pady=5)

	# Creating a message for non-response rate  
	non_response_message = Label(proportion_frame,text= "Expected non-response rate (needed for adjustment and 5%  if not known)")
	non_response_message.grid(row=4, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for non response rate  
	nr = Entry(proportion_frame)
	nr.grid(row=4, column=2,pady=5)

	# Creating a message for design effect adjustment  
	design_effect = Label(proportion_frame,text= "Design effect (needed for adjustment, 2 for two stages cluster with no prior information)")
	design_effect.grid(row=5, column=1,sticky = W,pady=5,padx=5)

	# Creating entry box for design effect  
	d_effect = Entry(proportion_frame)
	d_effect.grid(row=5, column=2,pady=5)

	# Creating a button for calculating initial sample size 
	calculate_button1 = Button(proportion_frame,text="Calculate initial Sample Size", command= ss_initial)
	calculate_button1.grid(row=6, column=1,pady=10)

	# Creating a button for calculating final sample size 
	calculate_button1 = Button(proportion_frame,text="Calculate final Sample Size", command= adjustment)
	calculate_button1.grid(row=7, column=1,pady=10)

	#  Creating a response button for the first sample size 
	response_label=Label(proportion_frame,text="")
	response_label.grid(row=6, column=2,pady=10)

	# Creating a response button for the final  sample size 
	response_label1=Label(proportion_frame,text="")
	response_label1.grid(row=7, column=2,pady=10)

	# Creating a response button for mininum sample recommended 
	response_label2=Label(proportion_frame,text="")
	response_label2.grid(row=8, column=2,pady=5)

	# Creating my clear and reset entry button 
	reset = Button(proportion_frame,text='Clear & reset all entries', command=reset_entry)
	reset.grid(row=9, column=1,pady=10)
#____________________________________________________________________________
# Creating my  team function 
def team  ():
	hide_frame()
	team_frame.pack(fill="both",expand=1)

	# Creating my temporary message 
	message = Label(team_frame,text= "Under construction")
	message.grid(row=1, column=1,sticky = W,pady=5,padx=5)
#____________________________________________________________________________
# Creating my cost function
def cost ():
	hide_frame()
	cost_frame.pack(fill="both",expand=1)

	# Creating my temporary message 
	message = Label(cost_frame,text= "Under construction")
	message.grid(row=1, column=1,sticky = W,pady=5,padx=5)
#____________________________________________________________________________
# Creating my Main menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Creating my sample size menu items
sample_size_menu = Menu(my_menu,background='purple', fg='white')
my_menu.add_cascade(label="Sample Size calculator",menu=sample_size_menu)
sample_size_menu.add_command(label="Total indicator",command=total)
sample_size_menu.add_command(label="Mean indicator",command=mean)
sample_size_menu.add_command(label="Proportion indicator",command=proportion)
sample_size_menu.add_separator()
sample_size_menu.add_command(label="Exit", command=root.quit)

# Creating my budget menu items
budget_menu = Menu(my_menu,background='purple', fg='white')
my_menu.add_cascade(label="Budget & Teaming",menu=budget_menu)
budget_menu.add_command(label="Teaming",command=team)
budget_menu.add_command(label="Cost",command=cost)
budget_menu.add_separator()
budget_menu.add_command(label="Exit",command=root.quit)

# Creating my Frames
total_frame =Frame(root, width=900, height=400)
mean_frame =Frame(root, width=900, height=400)
proportion_frame =Frame(root, width=900, height=400)
team_frame =Frame(root, width=800, height=400)
cost_frame =Frame(root, width=800, height=400)

# hide frame function and destroying widgets
def hide_frame(): 

	# destroying  the children widget in each of my frames
	for widget in total_frame.winfo_children():
		widget.destroy()
	for widget in mean_frame.winfo_children():
		widget.destroy()
	for widget in proportion_frame.winfo_children():
		widget.destroy()
	for widget in team_frame.winfo_children():
		widget.destroy()
	for widget in cost_frame.winfo_children():
		widget.destroy()
	
	# hiding my frames
	total_frame.pack_forget()
	mean_frame.pack_forget()
	proportion_frame.pack_forget()	
	team_frame.pack_forget()
	cost_frame.pack_forget()
	


root.mainloop()