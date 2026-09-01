'''
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
'''

from mysql.connector import *

con = None
cur = None

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

    if con is not None:
        con.rollback()

    print("There is a problem:", e)

finally:

    if cur is not None:
        cur.close()

    if con is not None:
        con.close()