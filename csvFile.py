import csv
f=open("Employee","w",newline='')
w=csv.writer(f)
w.writerow(["Name","Age","course"])
w.writerow(["Kajal","21","AIML"])
f.close()