from tkinter import *
import pytest
import sqlite3


kall=Tk()
kall.title("Home Page")
kall.config(bg="ghost white")
kall.geometry("1350x750+0+0")


# Create a databases or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()



'''
c.execute(""" CREATE TABLE addresses(
      first_name text,
      last_name text,
      address text,
      dob text,
      fathers_name text,
      birth_place text,
      ward_no integer,
      municipality text,
      gender text,
) """)
'''

# Create submit button for databases
def add():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:e1, :e2, :e3, :e4, :e5, :e6, :e7, :e8, :e9)",{
        "e1":e1.get(),
        "e2": e2.get(),
        "e3": e3.get(),
        "e4": e4.get(),
        "e5": e5.get(),
        "e6": e6.get(),
        "e7": e7.get(),
        "e8": e8.get(),
        "e9": e9.get(),
    })

    conn.commit()

    conn.close()

    # clear the text boxes
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)



def show():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)

    # Loop through the results
    print_record=''
    for record in records:
        print_record += str(record[0]) + ' '  + ' ' +str(record[5]) + ' ' +str(record[6]) + ' ' +str(record[7]) + ' ' +str(record[8]) + ' ' +str(record[9])  + "\n"
    query_label = Label(frame2, text=print_record)
    query_label.grid()


    conn.commit()
    conn.close()

def delete():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + del_entry.get())
    print("deleted sucessfully")

    # query of databases
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)

    # Loop through the results
    print_record = ''
    for record in records:
        print_record +=  str(record[0]) +  ' ' +str(record[5]) + ' ' +str(record[6]) + ' ' +str(record[7]) + ' ' +str(record[8]) + ' ' +str(record[9]) +  "\n"
    query_label = Label(frame2, text=print_record)
    query_label.grid()

    conn.commit()
    conn.close()

# Create edit function to update a record
def edit():

    global bikks

    bikks = Tk()
    bikks.title('Update Data')
    bikks.geometry('300x480')

    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = del_entry.get()

    # query of the database
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

    records = c.fetchall()

    #Creating global variable for all text boxes
    global e1_bikks
    global e2_bikks
    global e3_bikks
    global e4_bikks
    global e5_bikks
    global e6_bikks
    global e7_bikks
    global e8_bikks
    global e9_bikks





    label2=Label(bikks,text="Enter the details ",font=("times", "30", "bold"),bg="grey")
    label2.grid(row=0,column=1)
    name_label_bikks = Label(frame1, text="Name",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
    name_label_bikks.grid(row=1, column=1, sticky="w")
    e1_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e1_bikks.grid(row=1, column=2, sticky="w")

    last_label_bikks = Label(frame1, text="Caste",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
    last_label_bikks.grid(row=2, column=1, sticky="w")
    e2_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e2_bikks.grid(row=2, column=2, sticky="w")

    Address_label_bikks = Label(frame1, text="Permanent Address",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
    Address_label_bikks.grid(row=3, column=1, sticky="w")
    e3_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e3_bikks.grid(row=3, column=2, sticky="w")

    dob_label_bikks = Label(frame1, text="D.O.B",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
    dob_label_bikks.grid(row=4, column=1, sticky="w")
    e4_bikks_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e4_bikks_bikks.grid(row=4, column=2, sticky="w")

    fathersName_label_bikks = Label(frame1, text="Father's Name",padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
    fathersName_label_bikks.grid(row=5, column=1, sticky="w")
    e5_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e5_bikks.grid(row=5, column=2, sticky="w")

    birthplace_label_bikks = Label(frame1, text="Birth Place",padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
    birthplace_label_bikks.grid(row=6, column=1, sticky="w")
    e6_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e6_bikks.grid(row=6, column=2, sticky="w")

    ward_label_bikks = Label(frame1, text="Ward no.", padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
    ward_label_bikks.grid(row=7, column=1, sticky="w")
    e7_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e7_bikks.grid(row=7, column=2, sticky="w")

    municipality_label_bikks = Label(frame1, text="Municipality", padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
    municipality_label_bikks.grid(row=8, column=1, sticky="w")
    e8_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e8_bikks.grid(row=8, column=2, sticky="w")

    gender_label_bikks = Label(frame1, text="Gender", padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
    gender_label_bikks.grid(row=9, column=1, sticky="w")
    e9_bikks = Entry(frame1, font=("times", "25", "bold"),width=25)
    e9_bikks.grid(row=9, column=2, sticky="w")

    # loop through the results
    for record in records:
        e1_bikks.insert(0, record[0])
        e2_bikks.insert(0, record[0])
        e3_bikks.insert(0, record[0])
        e4_bikks.insert(0, record[0])
        e5_bikks.insert(0, record[0])
        e6_bikks.insert(0, record[0])
        e7_bikks.insert(0, record[0])
        e8_bikks.insert(0, record[0])
        e9_bikks.insert(0, record[0])







    # Create a update button
    edit_btn = Button(bikks, text=" SAVE ", command=update)
    edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

def update():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    record_id = del_entry.get()
    c.execute(""" UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        dob = :dob,
        fathers_name = :father,
        birth_place = :birthplace,
        ward_no = :ward,
        municipality = :municipality,
        gender = :gender,
         WHERE oid = :oid""",
         {'first': e1.get(),
          'last': e2.get(),
          'address': e3.get(),
          'dob': e4.get(),
          'father': e5.get(),
          'birthplace': e6.get(),
          'ward': e7.get(),
          'municipality': e8.get(),
          'gender': e9.get(),
          'oid': record_id
               }
    )
    conn.commit()
    conn.close()



#============================= creating the frames =================================
main_frame=Frame(kall, bg="cadet blue")
main_frame.grid()
label1 = Label(main_frame, text="CITIZEN CERTIFICATE DATA ENTRY", bg="yellow", font=("times", "20", "bold"))
label1.pack(side=TOP)
frame1 = Frame(main_frame, width=500, pady=20, height=650, bd=2, bg="grey", relief=RIDGE)
frame1.pack(side=LEFT)
frame2 = Frame(main_frame, width=400, pady=20, height=650, bd=2, bg="grey", relief=RIDGE)
frame2.pack(side=RIGHT)

#============================ creating the label and the entries in the frame 1 =====================

label2=Label(frame1,text="Enter the details ",font=("times", "30", "bold"),bg="grey")
label2.grid(row=0,column=1)
name_label = Label(frame1, text="Name",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
name_label.grid(row=1, column=1, sticky="w")
e1 = Entry(frame1, font=("times", "25", "bold"),width=25)
e1.grid(row=1, column=2, sticky="w")

last_label = Label(frame1, text="Caste",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
last_label.grid(row=2, column=1, sticky="w")
e2 = Entry(frame1, font=("times", "25", "bold"),width=25)
e2.grid(row=2, column=2, sticky="w")

Address_label = Label(frame1, text="Permanent Address",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
Address_label.grid(row=3, column=1, sticky="w")
e3 = Entry(frame1, font=("times", "25", "bold"),width=25)
e3.grid(row=3, column=2, sticky="w")

dob_label = Label(frame1, text="D.O.B",padx=2, pady=3,font=("times", "25", "bold"),bg="grey")
dob_label.grid(row=4, column=1, sticky="w")
e4 = Entry(frame1, font=("times", "25", "bold"),width=25)
e4.grid(row=4, column=2, sticky="w")

fathersName_label = Label(frame1, text="Father's Name",padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
fathersName_label.grid(row=5, column=1, sticky="w")
e5 = Entry(frame1, font=("times", "25", "bold"),width=25)
e5.grid(row=5, column=2, sticky="w")

birthplace_label = Label(frame1, text="Birth Place",padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
birthplace_label.grid(row=6, column=1, sticky="w")
e6 = Entry(frame1, font=("times", "25", "bold"),width=25)
e6.grid(row=6, column=2, sticky="w")

ward_label = Label(frame1, text="Ward no.", padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
ward_label.grid(row=7, column=1, sticky="w")
e7 = Entry(frame1, font=("times", "25", "bold"),width=25)
e7.grid(row=7, column=2, sticky="w")

municipality_label = Label(frame1, text="Municipality", padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
municipality_label.grid(row=8, column=1, sticky="w")
e8 = Entry(frame1, font=("times", "25", "bold"),width=25)
e8.grid(row=8, column=2, sticky="w")

gender_label = Label(frame1, text="Gender", padx=2, pady=3, font=("times", "25", "bold"),bg="grey")
gender_label.grid(row=9, column=1, sticky="w")
e9 = Entry(frame1, font=("times", "25", "bold"),width=25)
e9.grid(row=9, column=2, sticky="w")

#====================== creating the buttons ==========================================================\

add_button= Button(frame1, text="ADD",font=("times", "25", "bold"),bg="yellow", command=add())
add_button.grid(row=10,column=0)

add_button = Button(frame1, text="Show", font=("times", "25", "bold"), bg="yellow", command=show())
add_button.grid(row=10, column=1, sticky="e")

#====================== filling the second frame ===========================================================

delete_button=Button(frame2,text="delete id", font=("times", "25", "bold"), bg="yellow", command=delete())
delete_button.grid(row=0, column=0)
del_entry= Entry(frame2, font=("times", "25", "bold"), width=25)
del_entry.grid(row=0, column=1, sticky="w")

update_button = Button(frame2, text="update id", font=("times", "25", "bold"), bg="yellow", command=edit())
update_button.grid(row=1, column=0)
e11= Entry(frame2, font=("times", "25", "bold"), width=25)
e11.grid(row=1, column=1, sticky="w")

label3= Label(frame2, text="citizens details",font=("times", "25", "bold"),bg="yellow")
label3.grid(row=3,column=1)






mainloop()


