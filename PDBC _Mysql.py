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
# for db in cur:
#     print(db)
# if con.is_connected():
#     print("connected")
# else:
#     print("Sorry database cannt be connected")
    
# con.close()