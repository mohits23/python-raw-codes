def palarm(n):
    #print("\tn=",n)
    m=n
    s=0
    s1=0
    while n != 0:
        re=n%10
        s=(s*10)+re  # for palindrome
        #print("\t\ts=",s)
        s1=(re**3)+s1  #for armstrong
        #print("\t\ts1=",s1)
        n=n//10
            
    #print("\ts=",s)
    #print("\ts1=",s1)
    flag=[0,0]
    if m == s:
        flag[0]=1
    
    if m ==  s1:
        flag[1]=1
        
    return flag
    
    '''
    if flag1==1 and flag2==0:
        print("\n\tNumber Is Only Palindrome !")
    elif flag1==0 and flag2==1:
        print("\n\tNumber Is Only Armstrong !")
    elif flag1==1 and flag2==1:
        print("\n\tWonderful! Number Is Palindrome AS Well As Armstrong.")
    elif flag1==0 and flag2==0:
        print("\n\tNumber Is Neither Palindrome Nor Armstrong !")
    '''
temp=0
for i in range(2,1001):  # Here, x will start from 0
    res=palarm(i)
    if res[0]==1 and res[1]==1:
        temp=1
        win=i
        break

if temp == 1:
    print("\n\n\tWonderful! ",i,"is Both Palindrome As Well As Armstrong.")
else:
    print("\n\tOOps! No Such Number Found.")
    
