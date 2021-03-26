                        # Java Equivalent Problem

N = int(input())
sum = 0
for i in range(N):
    x = int(input())
    strg = str( int((1<<1)**x) )
    strg = strg[3:] if len(strg) > 2 else strg
    if len(strg) != 0:
        sum += int(strg)

print(sum%100)
