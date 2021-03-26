N = int(input())
s1 = str(input())
s2 = str(input())
temp = N
a1 = []
a2 = []

for i in range(N):
    a1.append(s1[i])
    a2.append(s2[i])

flag = 0
i = 0
while True:
    j = 0
    while j < len(a2):
        if a1[i] == a2[j]:
            temp = temp - 1
            flag = 1
            a1.pop(i)
            a2.pop(j)
            break
        j = j+ 1
    if flag == 1:
        i = 0
    else:
        break
    flag = 0

print(temp)
        
        
    
