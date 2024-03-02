import pyodbc

connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-3MRTNDB\AARYA;' 
                            'Database=demo;' 'Trusted_connection=yes;')

def read(connection):
    cursor = connection.cursor()
    print('read')
    cursor.execute('SELECT * FROM names')
    for row in cursor:
        print(row)
    connection.commit()    
def write(connection):
    cursor = connection.cursor()
    print('write')
    firstname=input("Enter First Name:")
    lastname=input("Enter Last Name:")
    cursor.execute('insert into names(FName, LName) values(?,?)', (firstname,lastname))
    read(connection)
    connection.commit()

write(connection)