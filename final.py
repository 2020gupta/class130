import csv
data1=[]
data2=[]
with open("data1.csv")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)
with open("data2_sorted.csv")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)
h1=data1[0]
p1=data1[1:]
h2=data2[0]
p2=data2[1:]
h=h1+h2
p=[]
for index,row in enumerate(p1):
    p.append(p1[index]+p2[index])
with open ("final.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p)
    