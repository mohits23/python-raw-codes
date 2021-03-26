def jakson(a,r,c,n,m):
    total = 0
    i = 0
    for ele1 in a[r]:
        if i == c-1 and c-1 >= 0:
            if ele1 == 1:
                total = total + 1
        if i == c+1 and c+1 < m:
            if ele1 == 1:
                total = total + 1
        i = i + 1
    
    if r == 0:
        i = 0
        for ele2 in a[r+1]:
            if i == c-1 and c-1 >= 0:
                if ele2 == 1:
                    total = total + 1
            if i == c:
                if ele2 == 1:
                    total = total + 1
            if i == c+1 and c+1 < m:
                if ele2 == 1:
                    total = total + 1
            i = i + 1

    if r == n-1:
        i = 0
        for ele3 in a[r-1]:
            if i == c-1 and c-1 >= 0:
                if ele3 == 1:
                    total = total + 1
            if i == c:
                if ele3 == 1:
                    total = total + 1
            if i == c+1 and c+1 < m:
                if ele3 == 1:
                    total = total + 1
            i = i + 1
        

    if r != 0 and r != n-1:
        i = 0
        for ele4 in a[r+1]:
            if i == c-1 and c-1 >= 0:
                if ele4 == 1:
                    total = total + 1
            if i == c:
                if ele4 == 1:
                    total = total + 1
            if i == c+1 and c+1 < m:
                if ele4 == 1:
                    total = total + 1
            i = i + 1

        i = 0
        for ele5 in a[r-1]:
            if i == c-1 and c-1 >= 0:
                if ele5 == 1:
                    total = total + 1
            if i == c:
                if ele5 == 1:
                    total = total + 1
            if i == c+1 and c+1 < m:
                if ele5 == 1:
                    total = total + 1
            i = i + 1
            
            
    return(total)
            
            

N, M = input().split()
N, M = [int(N), int(M)]

a = []

for i in range(N):

    elements = []
    elements = input().split()
    for j in range(M):
        elements[j] = int(elements[j])
    a.append(elements)


count = 0
for i in range(N):
    for j in range(M):
        #if i == 0 and j == 0:
        #continue
        if a[i][j] == 1:
            r = i
            c = j
            temp = jakson(a,r,c,N,M)
            if temp > 0:
                count = count + temp                
                print(f"{r}:{c} = {count}")
                count = 0
