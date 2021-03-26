                        # OBSTACLES GAME PROBLEM            
                
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
q = 0
h = []
A = [ [str(input()) for j in range(N)] for i in range(N) ]
for i in range(N):    
    for j in range(N):
        print(A[i][j],end = " ")
    print("\n")

for i in range(N):    
    for j in range(N):
        print("\n",i," ",j)
        if A[i][j] == 'R':
            if i-1 >= 0 and j-1 >= 0:
                if A[i-1][j-1] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i-1][j-1] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i-1][j-1] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i-1][j-1] == 'W':
                    obs4 += 1
                    h.append('W')

            if i-1 >= 0:        
                if A[i-1][j] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i-1][j] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i-1][j] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i-1][j] == 'W':
                    obs4 += 1
                    h.append('W')

            if i-1 >= 0 and j+1 < N:
                if A[i-1][j+1] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i-1][j+1] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i-1][j+1] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i-1][j+1] == 'W':
                    obs4 += 1
                    h.append('W')

            if j+1 < N:
                if A[i][j+1] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i][j+1] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i][j+1] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i][j+1] == 'W':
                    obs4 += 1
                    h.append('W')

            if i+1 < N and j+1 < N:
                if A[i+1][j+1] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i+1][j+1] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i+1][j+1] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i+1][j+1] == 'W':
                    obs4 += 1
                    h.append('W')
        
            if i+1 < N:
                if A[i+1][j] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i+1][j] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i+1][j] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i+1][j] == 'W':
                    obs4 += 1
                    h.append('W')
            
            if i+1 < N and j-1 >= 0:
                if A[i+1][j-1] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i+1][j-1] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i+1][j-1] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i+1][j-1] == 'W':
                    obs4 += 1
                    h.append('W')

            if j-1 >= 0:
                if A[i][j-1] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i][j-1] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i][j-1] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i][j-1] == 'W':
                    obs4 += 1
                    h.append('W')
        
            if i-1 >= 0 and j-1 >= 0:
                if A[i-1][j-1] == 'L':
                    obs1 += 1
                    h.append('L')
                if A[i-1][j-1] == 'S':
                    obs2 += 1
                    h.append('S')
                if A[i-1][j-1] == 'T':
                    obs3 += 1
                    h.append('T')
                if A[i-1][j-1] == 'W':
                    obs4 += 1
                    h.append('W')

            obstacles(obs1, obs2, obs3, obs4)  
            '''h.sort()
            for q in range(len(h)):
                print(h[i],end = ' ')
            h.clear()'''
            obs1 = 0
            obs2 = 0
            obs3 = 0
            obs4 = 0   

    print("\n")
    


