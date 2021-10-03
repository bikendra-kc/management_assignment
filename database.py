import sqlite3

def studentData():
    con=sqlite3.connect("certificate.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS certificate(id INTEGER PRIMARY KEY,StdID text, Firstname text, Address text, dob text, father text, birth text, ward text, municipality text, gender text) ")
    con.commit()
    con.close()

def addStdRec(StdID, Firstname  ,Address , dob, father, birth, ward, municipality, gender ):
    con=sqlite3.connect('certificate.db')
    cur = con.cursor()
    cur.execute("INSERT INTO certificate VALUES (NULL,?,?,?,?,?,?,?,?,?)",(StdID, Firstname ,Address , dob, father, birth, ward, municipality, gender ))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect('certificate.db')
    cur=con.cursor()
    cur.execute("SELECT * FROM certificate")
    rows =cur.fetchall()
    con.close
    return rows

def deleteRec(id):
    con=sqlite3.connect("certificate.db")
    cur=con.cursor()
    cur.execute("DELETE FROM certificate WHERE id=?",(id,))
    con.commit()
    con.close



def dataUpdate(id,StdID="", Firstname ='',Address ='' , dob ='', father ='', birth ='', ward ='', municipality ='', gender ='' ):
    con=sqlite3.connect("certificate.db")
    cur=con.cursor()
    cur.execute("UPGRADE  certificate SET StdID=? OR Firstname =?  OR Address =? OR \
      dob =? OR father =? OR  birth =? OR  ward =? OR municipality =? OR gender =? ",(id,StdID, Firstname ,Address , dob, father, birth, ward, municipality, gender ))
    con.commit()
    con.close()

studentData()