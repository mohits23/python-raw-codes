N, M = input().split()
N, M = [int(N), int(M)]

a = []

for i in range(N):

    elements = []
    elements = input().split()
    for j in range(M):
        elements[j] = int(elements[j])
    a.append(elements)

for i in range(N):
    c = 0
    for j in range(M):
        if a[i][j] == 1:
            if j >= 0 and j < M:
                if j == 0:
                    if a[i][j+1] == 1:
                        c = c + 1
                if j == M-1:
                    if a[i][j-1] == 1:
                        c = c + 1
                else:
                    if a[i][j+1] == 1:
                        c = c + 1
                    if a[i][j-1] == 1:
                        c = c + 1
            if i >= 0 and i < N:
                if i == 0:
                    if a[i+1][j-1] == 1:
                        c = c + 1
                    if a[i+1][j] == 1:
                        c = c + 1
                    if a[i+1][j+1] == 1:
                        c = c + 1
                        
                if i == N-1:
                    if a[i-1][j-1] == 1:
                        c = c + 1
                    if a[i-1][j] == 1:
                        c = c + 1
                    if a[i-1][j+1] == 1:
                        c = c + 1
                else:
                    if a[i-1][j-1] == 1:
                        c = c + 1
                    if a[i-1][j] == 1:
                        c = c + 1
                    if a[i-1][j+1] == 1:
                        c = c + 1

                    if a[i+1][j-1] == 1:
                        c = c + 1
                    if a[i+1][j] == 1:
                        c = c + 1
                    if a[i+1][j+1] == 1:
                        c = c + 1
    print(c)
