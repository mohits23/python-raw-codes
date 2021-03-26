
def obstacles(n1, n2, n3, n4):
    for i in range(n1):
        print("L",end = " ")
    for i in range(n2):
        print("S",end = " ")
    for i in range(n3):
        print("T",end = " ")
    for i in range(n4):
        print("W",end = " ")    

N = int(input())
obs1 = 0
obs2 = 0
obs3 = 0
obs4 = 0
h = []
A = [ [str(input()) for j in range(N)] for i in range(N) ]

for i in range(N):
    for j in range(N):
        if A[i][j] == 'R':
            #if i-1 >= 0 or j-1 >= 0 or i+1 < N or j+1 < N :
            if A[i-1][j-2] == 'L' or A[i-1][j] == 'L' or A[i-1][j+1] == 'L' or A[i][j+1] == 'L' or A[i+1][j+1] == 'L' or A[i+1][j] == 'L' or A[i+1][j-1] == 'L' or A[i][j-1] == 'L':
                obs1 += 1
            if A[i-1][j-2] == 'S' or A[i-1][j] == 'S' or A[i-1][j+1] == 'S' or A[i][j+1] == 'S' or A[i+1][j+1] == 'S' or A[i+1][j] == 'S' or A[i+1][j-1] == 'S' or A[i][j-1] == 'S':
                obs2 += 1
            if A[i-1][j-2] == 'T' or A[i-1][j] == 'T' or A[i-1][j+1] == 'T' or A[i][j+1] == 'T' or A[i+1][j+1] == 'T' or A[i+1][j] == 'T' or A[i+1][j-1] == 'T' or A[i][j-1] == 'T':
                obs3 += 1
            if A[i-1][j-2] == 'W' or A[i-1][j] == 'W' or A[i-1][j+1] == 'W' or A[i][j+1] == 'W' or A[i+1][j+1] == 'W' or A[i+1][j] == 'W' or A[i+1][j-1] == 'W' or A[i][j-1] == 'W':
                obs4 += 1

        obstacles(obs1, obs2, obs3, obs4)

    print("\n")
    obs1 = 0
    obs2 = 0
    obs3 = 0
    obs4 = 0

        
