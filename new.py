import pypyodbc as odbc
DRIVER_NAME='SQL SERVER'
SERVER_NAME='DESKTOP-3MRTNDB\AARYA'
DATABASE_NAME='demo'

#id=<username>;
#pwd=<password>;

connection_string=f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATA={DATABASE_NAME};
    Trust_Connection=yes;

    """
conn=odbc.connect(connection_string)
print(conn)

