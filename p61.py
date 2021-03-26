S = int(input("Enter The No. Of Seats >>> "))
N = int(input("Enter The Size Of Contingent >>> "))
K = int(input("Enter People For Wet Seats >>> "))
M = int(input("Enter Blocks OF Seats >>> "))

block = []
for i in range(M):
    element = int(input())
    block.append(element)

n1 = N-K
k1 = K
temp = 0
count1 = 1

for i in range(M):
    c = 0
    count2 = count1
    #count1 = 
    for j in range(temp,M):
        if j%2 == 0:
            if n1 != 0:
                if n1 >= block[j]:
                    n1 = n1 - block[j]
                    c = c + block[j]
                    count2 = count2+ block[j]
                else:
                    c = c + n1
                    count2 = count2+ n1
                    n1 = 0
            '''elif n1 == 0:
                count2 = count2 + block[j]'''
                
        if j%2 != 0:
            if k1 != 0:
                if k1 >= block[j]:
                    k1 = k1 - block[j]
                    c = c + block[j]
                    count2 = count2 + block[j]
                else:
                    c = c + k1
                    count2 = count2+ k1
                    k1 = 0
            '''elif k1 == 0:
                count2 = count2 + block[j]'''

    temp = temp + 1
    n1 = N-K
    k1 = K

    #print("\n\tDifference = ",count2-count1)
    print("\n\tc = ",c)
    count1 = count1 + block[i]
    
    
                    
                    
            
