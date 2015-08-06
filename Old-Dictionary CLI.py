import sqlite3 as sql

db = sql.connect('dictionary.db')

with db:
	cursor = db.cursor()
	while True:
		query = raw_input("Enter a Query: ").upper()
		if query[0] == "A":
			cursor.execute("SELECT definition FROM a WHERE topic=?", (query,))
		elif query[0] == "B":
			cursor.execute("SELECT definition FROM b WHERE topic=?", (query,))
		elif query[0] == "C":
			cursor.execute("SELECT definition FROM c WHERE topic=?", (query,))
		elif query[0] == "D":
			cursor.execute("SELECT definition FROM d WHERE topic=?", (query,))	
		elif query[0] == "E":
			cursor.execute("SELECT definition FROM e WHERE topic=?", (query,))
		elif query[0] == "F":
			cursor.execute("SELECT definition FROM f WHERE topic=?", (query,))
		elif query[0] == "G":
			cursor.execute("SELECT definition FROM g WHERE topic=?", (query,))
		elif query[0] == "H":
			cursor.execute("SELECT definition FROM h WHERE topic=?", (query,))
		elif query[0] == "I":
			cursor.execute("SELECT definition FROM i WHERE topic=?", (query,))
		elif query[0] == "J":
			cursor.execute("SELECT definition FROM j WHERE topic=?", (query,))
		elif query[0] == "K":
			cursor.execute("SELECT definition FROM k WHERE topic=?", (query,))
		elif query[0] == "L":
			cursor.execute("SELECT definition FROM l WHERE topic=?", (query,))
		elif query[0] == "M":
			cursor.execute("SELECT definition FROM m WHERE topic=?", (query,))
		elif query[0] == "N":
			cursor.execute("SELECT definition FROM n WHERE topic=?", (query,))
		elif query[0] == "O":
			cursor.execute("SELECT definition FROM o WHERE topic=?", (query,))
		elif query[0] == "P":
			cursor.execute("SELECT definition FROM p WHERE topic=?", (query,))
		elif query[0] == "Q":
			cursor.execute("SELECT definition FROM q WHERE topic=?", (query,))
		elif query[0] == "R":
			cursor.execute("SELECT definition FROM r WHERE topic=?", (query,))	
		elif query[0] == "S":
			cursor.execute("SELECT definition FROM s WHERE topic=?", (query,))
		elif query[0] == "T":
			cursor.execute("SELECT definition FROM t WHERE topic=?", (query,))
		elif query[0] == "U":
			cursor.execute("SELECT definition FROM u WHERE topic=?", (query,))
		elif query[0] == "V":
			cursor.execute("SELECT definition FROM v WHERE topic=?", (query,))
		elif query[0] == "W":
			cursor.execute("SELECT definition FROM w WHERE topic=?", (query,))
		elif query[0] == "X":
			cursor.execute("SELECT definition FROM x WHERE topic=?", (query,))
		elif query[0] == "Y":
			cursor.execute("SELECT definition FROM y WHERE topic=?", (query,))
		elif query[0] == "Z":
			cursor.execute("SELECT definition FROM z WHERE topic=?", (query,))
		
		rows = cursor.fetchall()
		for row in rows:
			print row[0]
