import sys
name = (sys.argv[1]).upper()
#year = sys.argv[2]
#month = sys.argv[3]

def fixed_width(item, width, pad_char):
          '''(str, int, str) -> str
          returns item in a fixed width string ending in pad_char's
          '''
          n = len(item)
          pad_len = width - n
          fixed_width_item = item + (pad_len * pad_char)
          return fixed_width_item

from datetime import datetime
date_format = "%Y-%m-%d %H:%M:%S.%f"

import sqlite3
con = sqlite3.connect('sakila.db')
cur = con.cursor()

cur.execute('SELECT first_name, last_name FROM Customer WHERE last_name=(?)',(name,))
cur.execute('SELECT Film.title, Rental.rental_date, Film.rental_rate, Rental.return_date, Film.rental_duration FROM Film JOIN Rental JOIN Inventory JOIN Customer WHERE Customer.customer_id=Rental.customer_id AND Inventory.inventory_id=rental.inventory_id AND Inventory.film_id=Film.film_id AND Inventory.store_id=Customer.store_id AND Customer.last_name=?',(name,) )
rows = cur.fetchall()
monthly_total = 0
for row in rows:
	film = fixed_width(str(row[0]).title(), 25, " ")
	rentaldate = fixed_width(str(row[1]), 20, " ")
	rentalrate = fixed_width(str(row[2]), 20, " ")
	returndate = fixed_width(str(row[3]), 20, " ")
	rentalduration = fixed_width(str(row[4]), 20, " ")
	rented = datetime.strptime(row[1], date_format)
	returned = datetime.strptime(row[3], date_format)
	diff = returned-rented
	latefee = fixed_width('               **late fee', 10, " ")
	none = fixed_width('', 25, " ")
	print (film, rentaldate, '$', rentalrate)
	#cur.execute('INSERT INTO Mastertable VALUES (?,?,?,?)',(film,none,rentaldate,rentalrate))
	if diff.days > row[4]:
		#cur.execute('INSERT INTO Mastertable VALUES (?,?,?,?)',(none,latefee,returndate,rentalrate))
		print (latefee, returndate, '$', rentalrate)
		monthly_total += row[2]
	monthly_total += row[2]

#QUESTIONS:
#	How do I change month to only show mm/dd/yyyy?
#	How can I automatically do .header on and .mode column?
#	How can I get it to check if the month they give is in the month segment of the date entry? For day?