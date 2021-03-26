def find_ing(st):
    chk = 0
    for i in range(len(st)):
        if st[i] == '5':
            chk = 1
            break
    return chk

with open("pythonfile.txt") as fp:
    flag = 0
    lino = fp.readlines()
    i = 0
    while fp.read() == '':
        if find_ing(lino[i]) == 1:
            flag = 1
            c = i
            break
        i += 1
    if flag == 1:
        print("Tup!! Found at %d" %c)
    else:
        print("Huh!!")
        
    
