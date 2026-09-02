'''

from mysql.connector import *

con = None
cur = None

try:
    # MySQL connect 
    con = connect(
        user='root',
        password='root',
        host='localhost',
        port=3306
    )

    print(con)

    # Cursor 
    cur = con.cursor()
निवडणे
    cur.execute("USE employee")

    # Table create करण्याची query
    query = """
    CREATE TABLE emp1(
        sno INT,
        name VARCHAR(20),
        sal INT
    )
    """

    # Query execute करणे
    cur.execute(query)

    print("Table created successfully")

except DatabaseError as e:

    if con is not None:
        con.rollback()

    print("There is a problem:", e)

finally:

    if cur is not None:
        cur.close()

    if con is not None:
        con.close()
  
  
#creating database
      
        
import mysql.connector

con = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    port=3306
)

print(con)
cur=con.cursor()
sql="show databases;"
cur.execute(sql)
for db in cur:
    print(db)
    
sql="create database FortuneCloud"
cur.close()
con.close()
# if con.is_connected():
#     print("connected")
# else:
#     print("Sorry database cannt be connected")
    
# con.close()

#multiple values inserted

from mysql.connector import *

con = None
cur = None
    # employee database 

try:
    con = connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='employee'
    )

    cur = con.cursor()

    query = """
    INSERT INTO emp1(sno, name, sal)
    VALUES (2, 'Jack', 15000),
           (3, 'Jill', 30000)
    """

    cur.execute(query)

    con.commit()

    print("Records Inserted Successfully")
    print(f"{cur.rowcount} records inserted")

except DatabaseError as e:
    print("There is a problem:", e)

finally:

    if cur is not None:
        cur.close()

    if con is not None:
        con.close()

     
#Update Employee program

from mysql.connector import *

con = None
cur = None

try:
    # MySQL connect 
    con = connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='employee'
    )

    # Cursor 
    cur = con.cursor()

    # Employee update query
    query = "UPDATE emp1 SET name='Harry' WHERE sno=3"

    # Query execute 
    cur.execute(query)

    # Changes permanently save 
    con.commit()

    print("Records updated successfully")
    print(f"{cur.rowcount} record updated")

# Database error handle 
except DatabaseError as e:

    if con is not None:
        con.rollback()

    print("There is a problem:", e)


finally:

    if cur is not None:
        cur.close()

    if con is not None:
        con.close()
        


#Program to insert record into database

from mysql.connector import *

con = None
cur = None

try:
    # MySQL ला connect करणे
    con = connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='employee'
    )

    print(con)

    # Cursor तयार करणे
    cur = con.cursor()

    # Record insert करण्याची query
    query = "INSERT INTO emp1(sno, name, sal) VALUES (1, 'Tom', 10000)"

    # Query execute करणे
    cur.execute(query)

    # Data permanently save करणे
    con.commit()

    print("Record Inserted Successfully")

except DatabaseError as e:

    if con is not None:
        con.rollback()

    print("There is a problem:", e)

finally:

    # Cursor बंद करणे
    if cur is not None:
        cur.close()

    # Connection बंद करणे
    if con is not None:
        con.close()



# Delete Employee program

from mysql.connector import *

con = None
cur = None

try:
    # MySQL ला connect करणे
    con = connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='employee'
    )

    # Cursor तयार करणे
    cur = con.cursor()

    # Employee record delete करण्याची query
    query = "DELETE FROM emp1 WHERE sno=3"

    # Query execute करणे
    cur.execute(query)

    # Changes permanently save करणे
    con.commit()

    print("Records deleted successfully")
    print(f"{cur.rowcount} record deleted")

except DatabaseError as e:

    # Error आल्यास changes cancel करणे
    if con is not None:
        con.rollback()

    print("There is a problem:", e)

finally:

    # Cursor बंद करणे
    if cur is not None:
        cur.close()

    # Connection बंद करणे
    if con is not None:
        con.close()
        

# SELECT ALL Employees

from mysql.connector import *

con = None
cur = None

try:
    # MySQL connect 
    con = connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='employee'
    )

    # Cursor 
    cur = con.cursor()

    # records select query
    query = "SELECT * FROM emp1"

    # Query execute 
    cur.execute(query)

    # records fetch 
    data = cur.fetchall()

    # record print 
    for d in data:
        print(d)

except DatabaseError as e:

    if con is not None:
        con.rollback()

    print("There is a problem:", e)

finally:

    # Cursor
    if cur is not None:
        cur.close()

    # Connection 
    if con is not None:
        con.close()
        
'''
# fetchone() 

from mysql.connector import *

con = None
cur = None

try:
    # MySQL connect 
    con = connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='employee'
    )

    # Cursor
    cur = con.cursor()

    # employees select query
    query = "SELECT * FROM emp1"

    # Query execute
    cur.execute(query)

    # record fetch 
    while True:

        data = cur.fetchone()

        if data is None:
            break

        print(data)

except DatabaseError as e:

    if con is not None:
        con.rollback()

    print("There is a problem:", e)

finally:

    # Cursor
    if cur is not None:
        cur.close()

    # Connection 
    if con is not None:
        con.close()