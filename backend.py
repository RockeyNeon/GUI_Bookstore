import sqlite3


class Database:

	def __init__(self, db):
		self.conn=sqlite3.connect(db) #create the database
		self.cur=self.conn.cursor()		#cursor object
		self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")		#table is created
		self.conn.commit()			#commit the changes made
					#close the window

	#create the insert function
	def insert(self, title, author, year, isbn):
		#cursor object
		self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))		#insert the values in the table
		self.conn.commit()			#commit the changes made

	# create the view object
	def view(self):
				#cursor object
		self.cur.execute("SELECT * FROM book")
		rows=self.cur.fetchall()  #fetch the selcted object using row variable
		return rows

	#create a function to search an entry
	def search(self, title="", author="", year="",isbn=""):
		#cursor object
		self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
		rows=self.cur.fetchall()  #fetch the selcted object using row variable
		return rows

	#create a function to delete a entry
	def delete(self, id):
				#cursor object
		self.cur.execute("DELETE FROM book WHERE id=?",(id,))		#insert the values in the table
		self.conn.commit()			#commit the changes made

	#create a function to update the details 
	def update(self,id,title, author, year, isbn):
			#cursor object
		self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))	
		self.conn.commit()			#commit the changes made

	def __del__(self):
		self.conn.close()

	#connect() 		#connect to the frontend when ever the frontend is call

	#insert ("The Earth","John Smith",1978,9865423)
	#delete(5)
	#update(4,"The moon","John batra", 1978,)
	#print(view())
	#print(search(author="John Smith"))