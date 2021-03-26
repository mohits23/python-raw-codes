'''A = []
N = 3
A = [ [str(input()) for j in range(N)] for i in range(N) ]

for i in range(N):
    for j in range(N):
        if (i-1 >= 0 and j-1 >= 0) and  (A[i][j] == 's' or A[i][j] == 'a'):
            print("True") 

name = [ 'Mohit','Jatin','Praveen','Abhishek']
name.sort()
for i in range(4):
    print(name[i],end = '')
    #print("\n") 

n = 5
a = []
count = 0
for i in range(n):
    ele = int(input())
    a[count] = ele
    count += 1

for i in range(n):
    print(a) 

a = []
for i in range(3):
    if i == 0:
        a.append('A')
    if i == 1:
        a.append('b')
    if i == 2:
        a.append('C')
    print(a) 

a = ["jko", "etdf", "dhgh"]
for i in range(len(a)):
    print(a[i],end =  ' ')

a.clear()
print(a)
for i in range(len(a)):
    print("~~~~~")
    print(a[i]) '''
    

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
        print("\n",i," ",j)
        if A[i][j] == 'R':
            if i-1 >= 0 and j-1 >= 0 and i+1 < N and j+1 < N :
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

        

'''if A[i-1][j-2] == 'L' or A[i-1][j-2] == 'S' or A[i-1][j-2] == 'T' or A[i-1][j-2] == 'W': 
if A[i-1][j] == 'L' or A[i-1][j] == 'S' or A[i-1][j] == 'T' or A[i-1][j] == 'W':
if A[i-1][j+1] == 'L' or A[i-1][j+1] == 'S' or A[i-1][j+1] == 'T' or A[i-1][j+1] == 'W':
if A[i][j+1] == 'L' or A[i][j+1] == 'S' or A[i][j+1] == 'T' or A[i][j+1] == 'W':
if A[i+1][j+1] == 'L' or A[i+1][j+1] == 'S' or A[i+1][j+1] == 'T' or A[i+1][j+1] == 'W':
if A[i+1][j] == 'L' or A[i+1][j] == 'S' or A[i+1][j] == 'T' or A[i+1][j] == 'W':
or A[i+1][j-1] == 'L' or A[i][j-1] == 'L': '''

'''if A[i-1][j-2] == 'L'
if A[i-1][j-2] == 'S'
if A[i-1][j-2] == 'T'
if A[i-1][j-2] == 'W'
or A[i-1][j-2] == 'S' or A[i-1][j-2] == 'T' or A[i-1][j-2] == 'W': 
if A[i-1][j] == 'L' or A[i-1][j] == 'S' or A[i-1][j] == 'T' or A[i-1][j] == 'W':
if A[i-1][j+1] == 'L' or A[i-1][j+1] == 'S' or A[i-1][j+1] == 'T' or A[i-1][j+1] == 'W':
if A[i][j+1] == 'L' or A[i][j+1] == 'S' or A[i][j+1] == 'T' or A[i][j+1] == 'W':
if A[i+1][j+1] == 'L' or A[i+1][j+1] == 'S' or A[i+1][j+1] == 'T' or A[i+1][j+1] == 'W':
if A[i+1][j] == 'L' or A[i+1][j] == 'S' or A[i+1][j] == 'T' or A[i+1][j] == 'W':
or A[i+1][j-1] == 'L' or A[i][j-1] == 'L': '''



if i-1 >= 0 and j-1 >= 0:
    if A[i-1][j-1] == 'L':
        obs1 += 1
    if A[i-1][j-1] == 'S':
        obs2 += 1
    if A[i-1][j-1] == 'T':
        obs3 += 1
    if A[i-1][j-1] == 'W':
        obs4 += 1

if i-1 >= 0:
    if A[i-1][j] == 'L':
        obs1 += 1
    if A[i-1][j] == 'S':
        obs2 += 1
    if A[i-1][j] == 'T':
        obs3 += 1
    if A[i-1][j] == 'W':
        obs4 += 1

if i-1 >= 0 and i+1 < N:
    if A[i-1][j+1] == 'L':
        obs1 += 1
    if A[i-1][j+1] == 'S':
        obs2 += 1
    if A[i-1][j+1] == 'T':
        obs3 += 1
    if A[i-1][j+1] == 'W':
        obs4 += 1

if j+1 < N:
    if A[i][j+1] == 'L':
        obs1 += 1
    if A[i][j+1] == 'S':
        obs2 += 1
    if A[i][j+1] == 'T':
        obs3 += 1
    if A[i][j+1] == 'W':
        obs4 += 1

if i+1 < N and j+1 < N:
    if A[i+1][j+1] == 'L':
        obs1 += 1
    if A[i+1][j+1] == 'S':
        obs2 += 1
    if A[i+1][j+1] == 'T':
        obs3 += 1
    if A[i+1][j+1] == 'W':
        obs4 += 1

if i+1 < N:
    if A[i+1][j] == 'L':
        obs1 += 1
    if A[i+1][j] == 'S':
        obs2 += 1
    if A[i+1][j] == 'T':
        obs3 += 1
    if A[i+1][j] == 'W':
        obs4 += 1

if i+1 < N and j-1 >= 0:
    if A[i+1][j-1] == 'L':
        obs1 += 1
    if A[i+1][j-1] == 'S':
        obs2 += 1
    if A[i+1][j-1] == 'T':
        obs3 += 1
    if A[i+1][j-1] == 'W':
        obs4 += 1

if j-1 >= 0:
    if A[i][j-1] == 'L':
        obs1 += 1
    if A[i][j-1] == 'S':
        obs2 += 1
    if A[i][j-1] == 'T':
        obs3 += 1
    if A[i][j-1] == 'W':
        obs4 += 1

if i-1 >= 0 and j-1 >= 0:
    if A[i-1][j-1] == 'L':
        obs1 += 1
    if A[i-1][j-1] == 'S':
        obs2 += 1
    if A[i-1][j-1] == 'T':
        obs3 += 1
    if A[i-1][j-1] == 'W':
        obs4 += 1

