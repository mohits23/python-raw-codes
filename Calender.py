                          # Calender Print

oddeve = 0
for j in range(1,12+1):  # Months  
    print("\n\t-: ",j," :-")
    for k in range(1,31+1):  # Days
        if j == 2 and k == 29:   # For February
            break
        if k == 31:
            if oddeve%2 != 0:  # For Odd Months
                break
        print(" ",k)
    if j == 7:
        oddeve = -1
    oddeve += 1
            
