import math

x_l = int(input("Enter x-axis for LifeGuard >>> "))
y_l = int(input("Enter y-axis for LifeGuard >>> "))
x_w = int(input("Enter x-axis for Drowning person >>> "))
y_w = int(input("Enter y-axis for Drowning person >>> "))
f = float(input("Enter Multiplying Factor >>> "))

inc = 0
for i in range(x_w+1):
    print("~~~",i)
    d = math.sqrt((x_w - i)**2 + y_w**2)
    print("\nd=",d)
    if inc == 0:
        small = d
    if inc > 0:
        #pos = i
        if d < small:
            #small = "{:.6f}".format(d)
            small = d
            pos = i
            print("\nsmall=",small)

    inc+=1

print("\n\tsmall = ",small)
print("\n\tpos = ",pos)
