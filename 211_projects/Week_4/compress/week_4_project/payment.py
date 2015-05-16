"""
payment.py: CIS 211 assignment 4.2, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

calculates and displays monthly payments given a year, loan amount, and interest rate.
interactive GUI used to assist with user input and display
"""
from tkinter import *

lock = 0

root = Tk()

label_amount = Label(root, text='Enter loan amount')
label_amount.grid(row=0,column=0)
label_interest = Label(root, text='Enter interest')
label_interest.grid(row=2,column=0)
label_years = Label(root, text='Enter length of loan (years)')
label_years.grid(row=4,column=0)

amount = Entry(root)
amount.grid(row=1,column=0)
interest = Entry(root)
interest.grid(row=3,column=0)
years = Entry(root)
years.grid(row=5,column=0)

def payment():
	"""
	calculates the monthly payment on a loan given the amount, number of years
	on the loan, and the interest rate on the load.
	"""
	global lock
	amount_x = int(amount.get())
	interest_x = float(interest.get())
	years_x = int(years.get())
	r = (interest_x)/100/12
	p = (years_x)*12
	payment_x = (r*amount_x)/(1-(1+r)**(-p))
	if lock == 0:
		monthly_payment.insert(0,('%.2f' % payment_x))
		lock += 1

monthly_payment = Entry(root)
monthly_payment.grid(row=7,column=0)

button = Button(root, text='Compute monthly payment', command=payment)
button.grid(row=6, column=0, pady = 10)

if __name__ == '__main__':
    root.mainloop()