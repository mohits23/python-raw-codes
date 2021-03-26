                    # LifeGuard - Drowning Person Problem

import math

x_l = int(input("Enter x-axis for LifeGuard >>> "))
y_l = int(input("Enter y-axis for LifeGuard >>> "))
x_w = int(input("Enter x-axis for Drowning person >>> "))
y_w = int(input("Enter y-axis for Drowning person >>> "))
f = float(input("Enter Multiplying Factor >>> "))

s_l = f
s_w = 1
pos = 0.0

inc = 0
for i in range(x_w + 1):

    d_l = math.sqrt((x_l - i)**2 + y_l**2)
    t_l = d_l / s_l
    d_w = math.sqrt((x_w - i)**2 + y_w**2)
    t_w = d_w / s_w

    total = t_l + t_w
    if inc == 0:
        small = total
        pos = "{:.6f}".format(i)
        
    print("\ntotal=",total)
    print("\nsmall=",small)

    if inc > 0:
        if total < small:
            small = total
            #pos = float(i)
            pos = "{:.6f}".format(i)
            

print("\n\tsmall=",small)
print("\n\tpos=",pos)

    
    

    
