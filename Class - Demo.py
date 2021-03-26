class Parent:
    def display(self,n):
        for i in range(n):
            print("Hellow World!")
         
class Child(Parent):
    def limit(self):
        N = int(input("Enter The Limit: "))
        super().display(N)
        

ob = Child()
ob.limit()
