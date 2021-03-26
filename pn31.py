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

def crack(p):
    count = 0
    temp = p
    while p != 0:
        if chk_sq(p) == 1:
            temp = temp - p
            count = count + 1
        p = p - 1

    return count
        

P = int(input())
Q = int(input())
R = int(input())
S = int(input())

flag = 0
p = p
r = R
c = 0
while P <= Q:
    





    
    if flag == 1:
        R = r
        
        
