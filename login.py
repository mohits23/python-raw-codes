with open("Try.txt","w",newline = '') as f:
    for i in range(2):
        if i == 0:
            f.writelines("mohit9090@gmail.com")
        else:
            f.writelines("jatin8989@gmail.com")
'''with open("Try.txt") as f:
    n = str(input())
    #var = f.readlines()
    while f.read(1):
        if n == f.read():
            print("Done!")
        else:
            print("Huh!")'''

with open("Try.txt","r",newline = '') as f:
    while f.read(1):
        print(f.read())
    print("\n\n")
    n = str(input())
    all_lines= f.readline()
    '''for each_line in all_lines:
        print(each_line)
        if each_line == n:
            print("Yeah!")
        else:
            print("Jerk!")'''
    while all_lines:
        if all_lines == n:
            print("Yeah!")
        else:
            print("Jerk!")
        all_lines = f.readline()
        
