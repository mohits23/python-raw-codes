                            # Prime Fibonacci

def digit(n):
    count = 0
    while n != 0:
        count+=1
        n = n/10
    return count

def check_prime(n):
    temp = 0
    for i in range(2,n//2+1):
        if n % i == 0:
            temp = 1;
            break
    if temp == 1:
        chk = 0
    elif temp == 0:
        chk = 1
    return chk

p1 = []
p2 = []
temp = 0
count = 0
total = 0
k = 0

n1, n2 = input().split()
n1, n2 = [int(n1), int(n2)]

for m in range(n1,n2+1):
    for i in range(2,m//2+1):
        if m % i == 0:
            temp = 1
            break
    if temp != 1:
        element1 = m
        p1.append(element1)
        count = k
        k += 1

    temp = 0

s = 0
for k in range(count+1):
    for i in range(count+1):
        if p1[k] == p1[i]:
            continue
        d = digit(p1[i])
        temp = (p1[k]*10**d) + p1[i]
        if check_prime(temp) == 1:
            p2[s] = temp
            s += 1

small = large = p2[0]
for i in range(s):
    if p2[i] > large:
        large = p2[i]
    if p2[i] < small:
        small = p2[i]

num1 = small
num2 = large
for i in range(1,s-2+1):
    total = num1 + num2
    num1 = num2
    num2 = total

print(total)






















        
