'''
import csv
f=open("Employee.csv","w",newline=' ')
w=csv.writer(f)
w.writerow(["Name","Age","course"])
w.writerow(["Kajal",21,"AIML"])
w.writerow(["Komal",21,"AIML"])
f.close()

import csv

f = open("Countries.csv","w",newline="")

myfields = ["State","Capital"]

writer = csv.DictWriter(f, fieldnames=myfields)

writer.writeheader()

writer.writerow({"State":"Maharashtra","Capital":"Mumbai"})
writer.writerow({"State":"Goa","Capital":"Panji"})

f.close()
'''
import csv
f = open("Countries.csv","w",newline="")

myfields = ["State","Capital"]

writer = csv.DictWriter(f, fieldnames=myfields)

writer.writeheader()

writer.writerow({"State":"Maharashtra","Capital":"Mumbai"})
writer.writerow({"State":"Goa","Capital":"Panji"})
f.close()


f = open("Countries.csv","r")
reader=csv.DictReader(f)
print(reader)
for row in reader:
    print(row['State'],"--",row['Capital'])
f.close()
