S = int(input("Ente7r The No. Of Seats >>> "))
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
bsum = 0
flag = 0

print("\n~~~~~~~~~~~~~~",n1,"\n~~~~~~~~~~~~~~~",k1)

for l in range(M):
    bsum = bsum + block[l]
    if l == 0:
        count = 0
    else:
        count = bsum
    for i in range(temp,M):

        if n1 == 0 and k1 == 0:
            break

        if i == M-1 and n1 != 0 and k1 != 0:
            flag = 1
            break
        
        if i%2 == 0:      # Even : Dry
            if n1 != 0:
                for j in range(block[i]+1):
                    if n1 == 0:
                        break
                    n1-=1
                    count+=1  # Counting Seat Numbers
                    
        elif i%2 != 0:     # Odd : Wet
            if k1 != 0:
                for j in range(block[i]+1):
                    if k1 == 0:
                        break
                    k1-=1
                    count+=1  # Counting Seat Numbers

    temp+=1
    if flag == 0:
        print("\n\tOutput = ",count-bsum)
    count = 0
    n1 = N-K
    k1 = K
    flag = 0
