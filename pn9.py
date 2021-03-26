M,N = input().split()
M, N = [int(M), int(N)]

a = []
b = []
for i in range(M):
    ele = []
    ele = input().split()
    a.append(list(map(lambda x: int(x), ele)))
        
L_temp = input().split()
L = list(map(lambda x: int(x), L_temp))

#print(M,"",N)
#print(a)
#print(L)

b = []
for i in range(M):
    ele = []
    for j in range(N):
        ele.append(0)
    b.append(ele)

#print(b)

m = M
n = N
for l in range(len(L)):
    if l%2 == 0:
        one_round = (m*2)+(n*2)-4
        if L[l] > one_round:
            steps = L[l] % one_round
        else:
            steps = L[l]

        for i in range(l,m):
            for j in range(l,n):

                if j == l and i >= l:
                    if i+steps <= m-1:
                        b[i+steps][j] = a[i][j]
                    else:
                        tem = (i+steps) - (m-1)
                        b[m-1][l+tem+1] = a[i][j]   #

                elif i == m-1 and j >= l:
                    if j+steps <= n-1:
                        b[i][j+steps] = a[i][j]
                    else:
                        tem = (j+steps) - (n-1)
                        b[m-1][(n-1)-tem-1] = a[i][j]

                elif j == n-1 and i >= l:
                    if i-steps >= l:
                        b[i-steps][j] = a[i][j]
                    else:
                        tem = abs(i-steps) - l
                        b[l][(n-1)-tem-1] = a[i][j]  #(m+1)

                elif i == l and j >= l:
                    if j-steps >= l:
                        b[i][j-steps] = a[i][j]
                    else:
                        tem = abs(j-steps) - l
                        b[l][l+temp+1] = a[i][j]

            m = m - 2
            n = n - 2
            


for i in range(M):
    print(end = '\n')
    for j in range(N):
        print(b[i][j], end = ' ')
