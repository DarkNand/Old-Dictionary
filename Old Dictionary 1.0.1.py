from gi.repository import Gtk
import sqlite3 as sql

class ParseGutenberg():
	def __init__(self, insert):
		self.db = sql.connect(insert)
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

class DictionaryObject(Gtk.Grid):
	def __init__(self, database):
		Gtk.Grid.__init__(self)
		self.database = database
		self.scroller = Gtk.ScrolledWindow()
		self.scroller.set_size_request(480, 480)
		self.textView = Gtk.TextView()
		self.textView.set_editable(False)
		self.textView.set_cursor_visible(False)
		self.textView.set_wrap_mode(Gtk.WrapMode(3))
		self.queryLabel = Gtk.Label("Enter a Topic and Press Go")
		self.queryLabel.set_justify(Gtk.Justification.CENTER)
		self.queryEntry = Gtk.Entry()
		self.goButton = Gtk.Button(label = 'Go')
		
		self.scroller.add(self.textView)
		self.attach(self.queryLabel, 0, 0, 5, 1)
		self.attach(self.queryEntry,0, 1, 3, 1)
		self.attach(self.goButton, 3, 1, 2, 1)
		self.attach(self.scroller, 0, 4, 3, 1)

		self.goButton.connect("clicked", self.goButton_callback)
		self.queryEntry.connect("activate", self.goButton_callback)
	
		
	def goButton_callback(self, widget):
		self.query = self.queryEntry.get_text().upper()
		buff = self.textView.get_buffer()
		try:
			definition = self.database.parse_database(self.query)
			buff.set_text(definition)
		except IndexError:
			pass
			
class DictionaryWindow(Gtk.Window):
	def __init__(self):	
		#This basically ascosiates the init method with a window
		Gtk.Window.__init__(self, title= "Old Dictionary")
		
		self.connect("delete-event", Gtk.main_quit)
		
		# Prevent window from resizing
		self.set_resizable(False)
		# Load databases
		self.database = ParseGutenberg('dictionary.db')

		# Header Buttons
		self.quitW = Gtk.Button(label = "Quit")
		self.nextPage = Gtk.Button(label = "Next Page")
		self.prevPage = Gtk.Button(label = "Previous Page")
		
		# Vbox, notebook, headerbar initialization
		self.vBox = Gtk.VBox()
		self.headerBar = Gtk.HeaderBar()
		self.notebook = Gtk.Notebook()
		self.vBox.pack_start(self.headerBar, True, True, 0)
		self.vBox.pack_start(self.notebook, True, True, 0)
		
		# Headerbar buttons
		self.headerBar.pack_start(self.quitW)
		self.headerBar.pack_end(self.nextPage)
		self.headerBar.pack_end(self.prevPage)
		# Add window to vBox
		self.add(self.vBox) #this works because self points to the window
		
		# Connect headerButtons
		self.quitW.connect("clicked", self.quit_window)
		self.nextPage.connect("clicked", self.next_page)
		self.prevPage.connect("clicked", self.prev_page)
		# Create pages
		pageOne = DictionaryObject(self.database)
		pageTwo = DictionaryObject(self.database)
		pageThree = DictionaryObject(self.database)
		pageFour = DictionaryObject(self.database)
		
		# Add pages
		self.notebook.append_page(pageOne)
		self.notebook.append_page(pageTwo)
		self.notebook.append_page(pageThree)
		self.notebook.append_page(pageFour)
		
	def quit_window(self, widget):
		Gtk.main_quit()
		
	def next_page(self, widget):
		self.notebook.next_page()
	
	def prev_page(self, widget):
		self.notebook.prev_page()


		
win = DictionaryWindow()

win.show_all()
Gtk.main()
