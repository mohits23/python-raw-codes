import csv

fields = ['Name','Class','Age']

rows = [['Shreya','5','11'],
         ['Kartik','12','19'],
         ['Nisha','9','14']]

with open('Stu.csv','w',newline = '') as cf:

    csvobj = csv.writer(cf)

    csvobj.writerow(fields)
    csvobj.writerows(rows)
    
with open('Stu.csv','r') as cf:

    csvread = csv.reader(cf)

    for lines in csvread:
        print(lines)

    print("\n")
    
    columns = csv.DictReader(cf)
    for data in columns:
        print(data['Class'])
