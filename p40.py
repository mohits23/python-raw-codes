import math

N = int(input("Enter The No. Of Rooms >>> "))
R1 = int(input("Enter Price Of TV Rooms >>> "))
R2 = int(input("Enter Price Of Non-TV Rooms >>> "))
T = int(input("Enter The Target Revenue >>>"))

oddeve = 0
flag = 0
patient = 0

for i in range(1,N+1):   # Rooms
    TV = R1*N
    for j in range(1,12+1):  # Months  
        for k in range(1,31+1):  # Days
            if j == 2 and k == 28:   # For February
                break
            if k == 30:
                if oddeve%2 != 0:  # For Odd Months
                    break
            oneday = (6-j)**2 + abs(k-15)
            patient += oneday

        oddeve += 1

    revenue = TV * patient
    if revenue >= T:
        nTV = i
        flag = 1
        break

print("\n\tpatient=",patient,"\n\trevenue=",revenue,"\n\tflag=",flag,"\n\ti=",i)

'''if flag == 1:
    print("\n\tNo. Of TVs : ", nTV )
elif flag == 0:
    print(N)'''
            
