from tkinter import *
from backend import Database

database=Database("books.db")

def get_selected_row(event):		#select particular entry and event help to select the particular event
	try:
		global select_tuple
		index=list1.curselection()[0]		#we are fetching the index because our function omly work on index 
		select_tuple=list1.get(index)
		#below code give the detail of selected entry in their appropriate box
		e1.delete(0,END)
		e1.insert(END,select_tuple[1])
		e2.delete(0,END)
		e2.insert(END, select_tuple[2])
		e3.delete(0,END)
		e3.insert(END, select_tuple[3])
		e4.delete(0,END)
		e4.insert(END, select_tuple[4])

	except IndexError:
		pass

def view_command(): 		 #function for the view command and show the detail in the list box
	list1.delete(0,END)			#so that the items not copy again and again
	for row in database.view():
		list1.insert(END, row) 	#END row insert the data at the end of the last row

def search_command():			#to search a particular entry and display in list box 
	list1.delete(0,END) 	#delete the earlier entries
	for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
							#due to stringvar in the entries we have to pass the get method so that we can get the inormation
		list1.insert(END,row)

def add_command():		#to add the entries into the database
	database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	list1.delete(0,END)
	list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():		#function to delete the entries
	database.delete(select_tuple[0])
	e1.delete(0,END)
	e2.delete(0,END)			#clear the entry area after deleting
	e3.delete(0,END)
	e4.delete(0,END)


def update_command():
	database.update(select_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	e1.delete(0,END)
	e2.delete(0,END)			#clear the entry area after updating
	e3.delete(0,END)
	e4.delete(0,END)


window=Tk()
window.wm_title("Book Store")

#form the labels
l1=Label(window, text="Title")
l1.grid(row=0, column=0)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)


#form the entry
title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

#create the list box
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2) #rowspan and columnspan help to ajust the box in all rows and columns


#create the scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

#configure the listbox and scrollbar
list1.configure(yscrollcommand=sb1.set) #y means y-axis
sb1.configure(command=list1.yview) #y means y-axis

#bind function which select a particular entry and asign to a function
list1.bind('<<ListboxSelect>>',get_selected_row)  #it pass 2 argument method and function to whom it will bind

#create the buttons
b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()