import csv
f=open("Employee","w")
w=csv.writer(f)
w.writerow(['Name','Age','course'])
f.close()