import sys
name = (sys.argv[1]).upper()
#year = sys.argv[2]
#month = sys.argv[3]



from datetime import datetime
date_format = "%Y-%m-%d %H:%M:%S.%f"

import sqlite3
con = sqlite3.connect('sakila.db')
cur = con.cursor()
#cur.execute('CREATE TABLE Keywords(Title TEXT, Late Fee TEXT, Sig_date TEXT, Price REAL)')
cur.execute('SELECT first_name, last_name FROM Customer WHERE last_name=(?)',(name,))
print (cur.fetchall())

cur.execute('SELECT Film.title, Rental.rental_date, Film.rental_rate, Rental.return_date, Film.rental_duration FROM Film JOIN Rental JOIN Inventory JOIN Customer WHERE Customer.customer_id=Rental.customer_id AND Inventory.inventory_id=rental.inventory_id AND Inventory.film_id=Film.film_id AND Inventory.store_id=Customer.store_id AND Customer.last_name=?',(name,) )
rows = cur.fetchall()
monthly_total = 0
for row in rows:
	rented = datetime.strptime(row[1], date_format)
	returned = datetime.strptime(row[3], date_format)
	diff = returned-rented
	print (row[0], rented)
	if diff.days > row[4]:
		print ("**late fee", row[3], row[2])
		monthly_total += row[2]
	monthly_total += row[2]
print ("Monthly Total:",monthly_total)