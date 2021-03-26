def jakson(a,r,c,n,m):

    #print('\n')
    total = 0
    if c-1 >= 0:
        if a[r][c-1] == 1:
            total = total + 1
    if c+1 < m:
        if a[r][c+1] == 1:
            total = total + 1
            
    if r == 0:
        if c-1 >= 0:
            if a[r+1][c-1] == 1:
                total = total + 1
        if a[r+1][c] == 1:
                total = total + 1
        if c+1 < m:
            if a[r+1][c+1] == 1:
                total = total + 1
                
    elif r == n-1:
        if c-1 >= 0:
            if a[r-1][c-1] == 1:
                total = total + 1
        if a[r-1][c] == 1:
                total = total + 1
        if c+1 < m:
            if a[r-1][c+1] == 1:
                total = total + 1

    elif r != 0 and r != n-1:
        if c-1 >= 0:
            if a[r+1][c-1] == 1:
                total = total + 1
        if a[r+1][c] == 1:
                total = total + 1
        if c+1 < m:
            if a[r+1][c+1] == 1:
                total = total + 1

        if c-1 >= 0:
            if a[r-1][c-1] == 1:
                total = total + 1
        if a[r-1][c] == 1:
                total = total + 1
        if c+1 < m:
            if a[r-1][c+1] == 1:
                total = total + 1

             
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

a[0][0] = 2


pool = []
for i in range(N):
    for j in range(M):
        if a[i][j] == 1:
            temp = jakson(a,i,j,N,M)
            if temp > 0:
                ele = []
                ele.append(i)
                ele.append(j)
                pool.append(ele)            
                print(f"{i+1}:{j+1} = {temp}")
                

print('\n')
large = pool[0]
for i in pool:
    if i > large:
        large = i

for i n pool:
    if large == i:
        
print(large)













