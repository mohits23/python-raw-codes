a=[13.0,14.5,21.8]
b=[14.5,13.0,13.0,21.8]
collide=0
for i in range(3):
    for k in range(4):
        if a[i] == b[k]:
            collide+=1
print("\n\t",collide)
            
    
    
