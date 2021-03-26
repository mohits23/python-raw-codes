import matplotlib.pyplot as plt

choice = 'y'
while choice == 'y' or choice =='Y':
    n = int(input("\nEnter Any Number: "))
    x = lambda x: x*x*x
    print("\nCube of the number:",x(n))
    choice = str(input(plt.plot("\n\tDo you want to do it again ?(Y/N): ")))
