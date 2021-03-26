import math

N = int(input("Enter The No. Of Rooms >>> "))
R1 = int(input("Enter Price Of TV Rooms >>> "))
R2 = int(input("Enter Price Of Non-TV Rooms >>> "))
Target = int(input("Enter The Target Revenue >>>"))

oddeve = 0
flag = 0
patient = 0
#temp = N
revenue = 0
inc = 0


'''inc = 0
for j in range(1,12+1):  # Months
        #print("\n\t-: ",j," :-")
        for k in range(1,31+1):  # Days
            if j == 2 and k == 29:   # For February
                break
            if k == 31:
                if oddeve%2 != 0:  # For Odd Months
                    break
            oneday = (6-j)**2 + abs(k-15)
            #print("\n\t", oneday )
            #patient += oneday
            #print(" ",k)
            if inc == 0:
                small = oneday
            if inc > 0:
                if oneday < small:
                    small = oneday
            inc+=1
            
        if j == 7:
            oddeve = -1
        oddeve += 1

print(small)
#print(temp) '''

for i in range(1,N+1):   # Rooms
    print("\n\t",i)
    for j in range(1,12+1):  # Months
        for k in range(1,31+1):  # Days
            if j == 2 and k == 29:   # For February
                break
            if k == 31:
                if oddeve%2 != 0:  # For Odd Months
                    break
            oneday = (6-j)**2 + abs(k-15)
            #print("\n\t", oneday )
            #patient += oneday
            #print(" ",k)
            temp = oneday
            if temp > 20:
                temp = 20
            drev = (R1*inc) + (R2*(temp-inc))
            print("\n-----",drev)
            print(" ",oneday)
            revenue = revenue + drev

        if j == 7:
            oddeve = -1
        oddeve += 1

    if revenue >= Target:
        TV = i
        flag = 1
        break
    else:
        inc = inc + 1
        #temp = temp - 1
    print("=",revenue)

#print("\n\tpatient=",patient,"\n\trevenue=",revenue,"\n\tflag=",flag,"\n\ti=",i,"\n\tTV=",TV)
#print("\n\npatient=", patient,"\nsmall=",small )

if flag == 1:
    print("\n\tNo. Of TVs : ", TV )
    print("\n\trevenue=", revenue)
elif flag == 0:
    print(N)
            
