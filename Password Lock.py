with open('Pass1.txt') as f:
    p = str(input("Enter The Password To Login >>> "))
    f.seek(0)
    
    if p == f.read():
        print("\tLogged In")
        c = str(input("Do You Want To Change The Password?(Y/N) "))
        if c == 'y' or c == 'Y':            
            old = str(input("Enter The Old Password >>> "))
            f.seek(0)
            if old == f.read():                
                f.close()                
                with open("Pass1.txt","w") as f:
                    f.write(str(input("Enter New Password >>> ")))
            else:
                print("Incorrect Old Password")
    else:
        print("Incorrect Passsword")
            
        
    
