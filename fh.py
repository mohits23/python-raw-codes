f = open("pythonfile.txt","w+")
for i in range(10):
    f.write("This is line %d\n " %(i+1) )
f.close()

f = open("pythonfile.txt","a+")
for i in range(2):
    f.write("Appended line %d\n" %(i+1) )
f.close()

#f = open("pythonfile.txt","r")
with open("pythonfile.txt") as f:
        while f.read(1):
            print(f.read())
f.close()

def finding(st):
    chk = 0
    for i in range(len(st)):
        if st[i] == ' This is line 4':
            chk = 1
    return chk

f = open("pythonfile.txt")
flag = 0
c = f.readlines()
print("\n\tt=",c[5])
