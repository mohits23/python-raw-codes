P = int(input())
Q = int(input())
R = int(input())
S = int(input())

def todo(l,w):
    count = 0
    while l != w:
        if l > w:
            l = l - w
            count = count + 1
        elif w > l:
            w = w - l
            count = count + 1

    return count+1

total = 0
while P <= Q:
    i = R
    while i <= S:
        temp = todo(P,i)    
        total = total + temp
        i = i + 1
    P = P + 1

print(total)
