a = [3,6,5,4,1,2]
b = ['a','b','c','d','e','f']
c = []
d = []
for i in range(len(a)):
    c.append('1')
    d.append(b[i])

count = 0
while True:
    for i in range(len(a)):
        c[a[i]-1] = b[i]
    
    for i in range(len(a)):
        b[i] = c[i]
    print('\n',b)
    count = count + 1
    if b == d:
        break
print(count)
