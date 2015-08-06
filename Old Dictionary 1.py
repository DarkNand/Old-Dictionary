from gi.repository import Gtk
import sqlite3 as sql

class ParseDatabase():
	def __init__(self):
		self.db = sql.connect('dictionary.db')
		self.cursor = self.db.cursor()
	
	def parse_database(self, topic):
		with self.db:
			self.query = topic
			if self.query[0] == "A":
				self.cursor.execute("SELECT definition FROM a WHERE topic=?", (self.query,))
			elif self.query[0] == "B":
				self.cursor.execute("SELECT definition FROM b WHERE topic=?", (self.query,))
			elif self.query[0] == "C":
				self.cursor.execute("SELECT definition FROM c WHERE topic=?", (self.query,))
			elif self.query[0] == "D":
				self.cursor.execute("SELECT definition FROM d WHERE topic=?", (self.query,))	
			elif self.query[0] == "E":
				self.cursor.execute("SELECT definition FROM e WHERE topic=?", (self.query,))
			elif self.query[0] == "F":
				self.cursor.execute("SELECT definition FROM f WHERE topic=?", (self.query,))
			elif self.query[0] == "G":
				self.cursor.execute("SELECT definition FROM g WHERE topic=?", (self.query,))
			elif self.query[0] == "H":
				self.cursor.execute("SELECT definition FROM h WHERE topic=?", (self.query,))
			elif self.query[0] == "I":
				self.cursor.execute("SELECT definition FROM i WHERE topic=?", (self.query,))
			elif self.query[0] == "J":
				self.cursor.execute("SELECT definition FROM j WHERE topic=?", (self.query,))
			elif self.query[0] == "K":
				self.cursor.execute("SELECT definition FROM k WHERE topic=?", (self.query,))
			elif self.query[0] == "L":
				self.cursor.execute("SELECT definition FROM l WHERE topic=?", (self.query,))
			elif self.query[0] == "M":
				self.cursor.execute("SELECT definition FROM m WHERE topic=?", (self.query,))
			elif self.query[0] == "N":
				self.cursor.execute("SELECT definition FROM n WHERE topic=?", (self.query,))
			elif self.query[0] == "O":
				self.cursor.execute("SELECT definition FROM o WHERE topic=?", (self.query,))
			elif self.query[0] == "P":
				self.cursor.execute("SELECT definition FROM p WHERE topic=?", (self.query,))
			elif self.query[0] == "Q":
				self.cursor.execute("SELECT definition FROM q WHERE topic=?", (self.query,))
			elif self.query[0] == "R":
				self.cursor.execute("SELECT definition FROM r WHERE topic=?", (self.query,))	
			elif self.query[0] == "S":
				self.cursor.execute("SELECT definition FROM s WHERE topic=?", (self.query,))
			elif self.query[0] == "T":
				self.cursor.execute("SELECT definition FROM t WHERE topic=?", (self.query,))
			elif self.query[0] == "U":
				self.cursor.execute("SELECT definition FROM u WHERE topic=?", (self.query,))
			elif self.query[0] == "V":
				self.cursor.execute("SELECT definition FROM v WHERE topic=?", (self.query,))
			elif self.query[0] == "W":
				self.cursor.execute("SELECT definition FROM w WHERE topic=?", (self.query,))
			elif self.query[0] == "X":
				self.cursor.execute("SELECT definition FROM x WHERE topic=?", (self.query,))
			elif self.query[0] == "Y":
				self.cursor.execute("SELECT definition FROM y WHERE topic=?", (self.query,))
			elif self.query[0] == "Z":
				self.cursor.execute("SELECT definition FROM z WHERE topic=?", (self.query,))
		
			rows = self.cursor.fetchall()
			
			for row in rows:
				self.definition =  row[0]
				return self.definition

class DictionaryWindow(Gtk.Window):
	def __init__(self):	
		#This basically ascosiates the init method with a window
		Gtk.Window.__init__(self, title= "Old Dictionary")
		
		self.database = ParseDatabase()
		
		# Create a grid and add it to the window
		grid = Gtk.Grid()
		self.add(grid) #this works because self points to the window
		self.connect("delete-event", Gtk.main_quit)
		
		#This is how you create children
		queryLabel = Gtk.Label("Enter a Topic and Press Go")
		queryLabel.set_justify(Gtk.Justification.CENTER)
		self.queryEntry = Gtk.Entry()
		self.goButton = Gtk.Button(label = 'Go')
		self.textView = Gtk.TextView()
		self.textView.set_editable(False)
		self.textView.set_cursor_visible(False)
		self.textView.set_wrap_mode(Gtk.WrapMode(3))
		self.scroller = Gtk.ScrolledWindow()
		self.scroller.set_size_request(480, 480) # FORCE BIGGER SIZE FOR TEXTVIEW
		self.scroller.add(self.textView)
		#This is how you link the buttons with methods
		self.goButton.connect("clicked", self.goButton_callback)
		self.queryEntry.connect("activate", self.goButton_callback)
		
		# grid.attach accepts a widget, column, row, width, height
		grid.attach(queryLabel, 0, 0, 5, 1)
		grid.attach(self.queryEntry, 0, 1, 3, 1)
		grid.attach(self.goButton, 3, 1, 1, 1)
		grid.attach(self.scroller, 0, 4, 4, 1)
		
	#The following are callback functions for the buttons
	def goButton_callback(self, widget):
		query = self.queryEntry.get_text().upper()
		buff = self.textView.get_buffer()
		definition = self.database.parse_database(query)
		try:
			buff.set_text(definition)
		except TypeError:
			pass
		
		
win = DictionaryWindow()
win.show_all()
Gtk.main()
				
