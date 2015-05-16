import sys
name = (sys.argv[1]).upper()
#year = sys.argv[2]
#month = sys.argv[3]

from datetime import datetime
date_format = "%Y-%m-%d %H:%M:%S.%f"

import sqlite3
con = sqlite3.connect('sakila.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Mastertable (Title TEXT, Late Fee TEXT, Sig_date TEXT, Price REAL)')
cur.execute('SELECT first_name, last_name FROM Customer WHERE last_name=(?)',(name,))
cur.execute('SELECT Film.title, Rental.rental_date, Film.rental_rate, Rental.return_date, Film.rental_duration FROM Film JOIN Rental JOIN Inventory JOIN Customer WHERE Customer.customer_id=Rental.customer_id AND Inventory.inventory_id=rental.inventory_id AND Inventory.film_id=Film.film_id AND Inventory.store_id=Customer.store_id AND Customer.last_name=?',(name,) )
rows = cur.fetchall()
monthly_total = 0
for row in rows:
	film = row[0]
	rentaldate = row[1]
	rentalrate = row[2]
	returndate = row[3]
	rentalduration = row[4]
	rented = datetime.strptime(row[1], date_format)
	returned = datetime.strptime(row[3], date_format)
	diff = returned-rented
	latefee = '**late fee'
	none = ''
	cur.execute('INSERT INTO Mastertable VALUES (?,?,?,?)',(film,none,rentaldate,rentalrate))
	if diff.days > rentalduration:
		cur.execute('INSERT INTO Mastertable VALUES (?,?,?,?)',(none,latefee,returndate,rentalrate))
		monthly_total += rentalrate
	monthly_total += rentalrate
cur.execute('INSERT INTO Mastertable VALUES (?,?,?,?)',('Monthly Total:',str(round(monthly_total,2)),none,none))
con.commit()
cur.execute('SELECT * FROM Mastertable')
con.commit()
print (cur.fetchall())

#QUESTIONS:
#	How do I change month to only show mm/dd/yyyy?
#	How can I automatically do .header on and .mode column?
#	How can I get it to check if the month they give is in the month segment of the date entry? For day?