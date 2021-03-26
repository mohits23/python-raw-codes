                        # Square Free Numbers Problem (Solved:-)
        ''' Test Cases >>> 20:3 // 72:3 // 29729700:63 // 62290800:31 //
                   691891200:63 // 523908000:31 // 290990700:255 ''' 
import math

def chk_sq(s):
    flag = 0
    for i in range(2,s//2 + 1):
        if s/i == math.sqrt(s):
            flag = 1
            break
    if flag == 1: # Perfect Square
        chk = 1
    else:         # Not Perfect Square  
        chk = 0

    return chk                

def sq_free(x):
    flag = 0
    for i in range(2,x + 1):
        if x % i == 0:
            #temp = int(math.sqrt(i)*10) % 10
            #if ( int(math.sqrt(i)*10) % 10 )   == 0:
            if chk_sq(i) == 1:
                flag = 1
                break
    if flag == 0:
        return 1  # Square Free
    else:
        return 0  # Not Square Free

N = int(input("Enter The Value >>> "))

count = 0

for i in range(2,N + 1):
    if N % i == 0:
        #print("\n\t",i)
        if sq_free(i) == 1:
            #print("~~~~~~",i)
            count+=1

print("\n\tcount = ",count)       
