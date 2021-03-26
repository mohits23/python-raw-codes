                            # Password Secured Program
import msvcrt

with open("Pass.txt") as file:
    st = str(input("\n Enter The Password To Login >>> "))
    print("\n\t~~~~~~~~~~~",file.read())

    if st == file.read():
            print("\n\t~~~~~~~~~~~",file.read())
            print("Logged In")
            print("\n\t~~~~~~~~~~~",file.read())
            c = str(input("Do You Want To Change The Pasword?(Y/N) "))
            print("\n\t~~~~~~~~~~~",file.read())
            if c == 'y' or c == 'Y':
                print("\n\t~~~~~~~~~~~",file.read())
                old = str(input("Enter The Old Password >>> "))
                print("\n\t~~~~~~~~~~~",file.read())
                if old == file.read():
                    with open("Pass.txt","w") as file:  
                        file.write(str(input("Enter New Password >>> ")))
                else:
                    print("Incorrect Old Password")
    else:
            print("Incorrect Password")
            
        

        
