"""
summary.py: CIS 211 assignment 6, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

prints report showing given customers monthly (or yearl) report, including movies rented and total fees
"""

import sys
name = (sys.argv[1]).upper()
year = sys.argv[2]
time_incr = "Monthly"
if len(sys.argv)==3:
	month = "FULL YEAR"
	time_incr = "Yearly"
elif len(sys.argv[3])<2:
	month = ("0"+str(sys.argv[3]))
elif len(sys.argv[3])==2:
	month = sys.argv[3]

def fixed_width(item, width, pad_char):
          '''(str, int, str) -> str
          returns item in a fixed width string ending in pad_char's
          '''
          n = len(item)
          pad_len = width - n
          fixed_width_item = item + (pad_len * pad_char)
          return fixed_width_item

from datetime import datetime
date_format= "%Y-%m-%d %H:%M:%S.%f"

import sqlite3
con = sqlite3.connect('sakila.db')
cur = con.cursor()

header = '\n----- Sakila DVD Rentals -----\n'
print (header)

cur.execute('SELECT first_name, last_name, customer_id, address, postal_code, email FROM Customer, Address WHERE Customer.address_id=Address.address_id AND (last_name=? OR customer_id=?)',(name,name,))
basic_info = cur.fetchall()
for row in basic_info:
	print (time_incr+" report for "+row[0].title()+' '+row[1].title()+'\n'+row[3]+' '+str(row[4])+'\n'+row[5]+'\n')

cur.execute('SELECT title, rental_date, rental_rate, return_date, rental_duration FROM Film, Inventory, Rental, Customer WHERE Customer.customer_id=Rental.customer_id AND Inventory.inventory_id=rental.inventory_id AND Inventory.film_id=Film.film_id AND (Customer.last_name=? or Customer.customer_id=?)',(name,name,))
rows = cur.fetchall()
monthly_total = 0
for row in rows:
	rentaldate_display = (' '+str(row[1])[5:7]+'/'+str(row[1])[8:10]+'/'+str(row[1])[0:4])
	returndate_display = (' '+str(row[3])[5:7]+'/'+str(row[3])[8:10]+'/'+str(row[3])[0:4])
	film = fixed_width(str(row[0]).title(), 25, " ")
	rentaldate = fixed_width(str(row[1]), 20, " ")
	rentalrate = fixed_width(str(row[2]), 20, " ")
	returndate = fixed_width(str(row[3]), 20, " ")
	rentalduration = fixed_width(str(row[4]), 20, " ")
	rented = datetime.strptime(row[1], date_format)
	if row[3]!=None:
		returned = datetime.strptime(row[3], date_format)
		diff = returned-rented
		latefee = fixed_width((" "*15)+'**late fee', 10, " ")
		none = fixed_width('', 25, " ")
		if (row[1])[0:4]==year:
			if (row[1])[5:7]==month:
				print (film+rentaldate_display+' $'+rentalrate)
				if diff.days > row[4]:
					print (latefee+returndate_display+' $'+rentalrate)
					monthly_total += row[2]
				monthly_total += row[2]
			if month=="FULL YEAR":
				print (film+rentaldate_display+' $'+rentalrate)
				if diff.days > row[4]:
					print (latefee+returndate_display+' $'+rentalrate)
					monthly_total += row[2]
				monthly_total += row[2]

print ('\n'+time_incr+' total:'+'$'+str(round(monthly_total,2))+'\n')
