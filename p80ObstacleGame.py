N = int(input("Enter The Dimension >>> "))

A = [ [str(input()) for j in range(N)] for i in range(N) ]

''' A S L D
    T R W R
    R M S R
    W R R M  '''

hurdles = []
for i in range(N):
    count = 0
    for j in range(N):
        if  i-1 >= 0 and j-1 >= 0:
            if A[i-1][j-1] == 'S' or A[i-1][j-1] == 'L' or A[i-1][j-1] == 'W' or A[i-1][j-1] == 'T':
                ele = A[i-1][j-1]
                hurdles.append(ele)
                
        if i+1 < N and j+1 < N:
            if A[i+1][j+1] == 'S' or A[i+1][j+1] == 'L' or A[i+1][j+1] == 'W' or A[i+1][j+1] == 'T':
                ele = A[i+1][j+1]
                hurdles.append(ele)

        if i-1 >= 0:
            if A[i+1][j+1] == 'S' or A[i+1][j+1] == 'L' or A[i+1][j+1] == 'W' or A[i+1][j+1] == 'T':
                ele = A[i+1][j+1]
                hurdles.append(ele)

        if i+1 < N:
            if A[i+1][j+1] == 'S' or A[i+1][j+1] == 'L' or A[i+1][j+1] == 'W' or A[i+1][j+1] == 'T':
                ele = A[i+1][j+1]
                hurdles.append(ele)

        if j-1 >= 0:
            if A[i+1][j+1] == 'S' or A[i+1][j+1] == 'L' or A[i+1][j+1] == 'W' or A[i+1][j+1] == 'T':
                ele = A[i+1][j+1]
                hurdles.append(ele)

        if j+1 < N:
            if A[i+1][j+1] == 'S' or A[i+1][j+1] == 'L' or A[i+1][j+1] == 'W' or A[i+1][j+1] == 'T':
                ele = A[i+1][j+1]
                hurdles.append(ele)
        
        hurdles.sort()
        print(hurdles,end = ' ')
        hurdles.clear()

    print("\n")
