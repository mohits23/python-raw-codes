''' Tab = 7 spaces'''

''' 97-122 = a-z
    65-90 = A-Z '''

''' On Desktop Screen :-
        Ctrl + N >>> Press 'T' >>> This PC will open. '''

''' Press "Alt + 2" To Create New Folder(s) '''

                            # Ternary Operators( if, else; same as [?, :] in 'C' ) In Python
a = 5
b = 4
c = 9

x = lambda a,b: a if a > b else b # For Largest Among 2 Values Using Ternary Operators
print( x(a,b) )

X = lambda a,b,c: a if (a > b) and (a > c) else b if (b > c) else c
print( X(a,b,c) )


                            # Nested "if - else" statement with Nested "and - or"
# Just Example:
    
if board[i][j] != 'X':
            if ( (j == 0 and board[i][j+1] == 0) or (j+1 < N and board[i][j-1] == 'X' and board[i][j+1] == 0) )  ''' 1st Mojor Part On Left ''' or ''' 2nd Major Part On Right '''  ( (i == 0 and board[i+1][j] == 0)  or (i+1 < N and board[i-1][j] == 'X' and board[i+1][j] == 0) ):
                board[i][j] = inc
                

                            # Using "print()" as "printf()" of 'C' in Python
a = 10
print("The value is %d" %(a+1))
               '''If there is any expression after '%'(just like in this case),
                    use of Parenthesis is mandatory,i.e.,
                expression should be kept in Parenthesis.'''


                            # Arrays
a=[11,12,13,14,15,16]
i=0
for element in a:
    print("Value",i+1,"=",element)
    i+=1

       ''' TO Remove All Elemnets Of A List, Do As :-
                 name.clear()   '''

  ## Input Using "split()"

x, y = input("Enter Two Values :- ").split()
x, y = int(x), int(y)
print("X = ", x+5)
print("Y = ", y+5)

 ## Most efficient methods to input many integers separated by space(or anything) in one line

a = [int(j) for j in input().split()] # Method 1 (Kickstart copy)
print(a)

        # [OR] #

b = list(map(lambda x: int(x),input().split())) # Method 2 (@msoriginals)
print(b)

        

                            # Declare An Empty Array(List)
a = []


                            # 2-D Array Input( Matrix Input )
                            
R = int(input("Enter The No. Of Rows >>> "))
C = int(input("Enter The No. Of Columns >>>"))
matrix = []
print("Enter The Elements Of Array : ")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input())
    matrix.append(a)

# [OR] One Liner Input Method :
#             \/
#             \/
# matrix = [ [int(input()) for j in range(C)] for i in range(R) ]

  # For Printing Matrix

for i in range(R):
    for j in range(C):
        print( matrix[i][j], end = " " )
                 ''' If [end = " "] is not used then output will be (Vertical):
                        1
                        2
                        3
                        4
             But If We Use [end = " "] is used then it will print
            the values Horizontally with 1 space[ " " can increase spaces] as:

                 Output :  1 2 3 4  '''

   # Input Method For N*N Square Matrix In One Line
          
N = 3  
a = [ input().split() for i in range(N) ]
print(a)

   # Input For M*N Matrix( @msoriginals )

r = 2
c = 3

a = []

for i in range(r):

    elements = []
    elements = input().split()
    for j in range(c):
        elements[j] = int(elements[j])
    a.append(elements)
    
for i in range(r):
    for j in range(c):
        print(a[i][j], end = ' ')
    print('\n')
    
print(a[1][0])
                 
                 
                            # Printing Alphabets Using chr()
    ''' chr(97) = 'a' [where 97 = 'a' and 122 = 'z' in ASCII]
        chr(65) = 'A' [where 65 = 'A' and 90 = 'Z' in ASCII]'''

for i in range(97,123):
    print( chr(i), end = ' ' )
    
    ''' ord(a) = 97 [ ord() returns the ASCII Code of the Chracter passed as Argument in ord() ]
        ord(A) = 65 '''

for i in range(ord('a'),ord('z')):
    print(i, end = ' ')                 

                            # Fuction and Input and "print()" in "return"
def deci(x):
    return print("\n\tx=",x)

deci(int(input("input >>> ")))


                            # Print Upto 6 Decimal Places
def deci(x):
    return print("{:.6f}".format(x) )  # [OR] return print( f'x = {"{:.6f}".format(x)}' )

deci(9.1234568)

                            # Can Compare an "integer" and a "float" value
a=50
b=50.43
if a > b:
    print(a)
elif b > a:
    print(b)

                            # New Way Of Finding The Smallest/Largest
                            # in an on-going loop / nested loop
                               #msoriginals
inc = 0
for j in range(1,12+1):  # Months
        #print("\n\t-: ",j," :-")
        for k in range(1,31+1):  # Days
            if j == 2 and k == 29:   # For February
                break
            if k == 31:
                if oddeve%2 != 0:  # For Odd Months
                    break
            oneday = (6-j)**2 + abs(k-15)
            #print("\n\t", oneday )
            #patient += oneday
            #print(" ",k)
            if inc == 0:
                small = oneday
            if inc > 0:
                if oneday < small:
                    small = oneday
            inc+=1
            
        if j == 7:
            oddeve = -1
        oddeve += 1

print(small)

'''******************************************************************************************************************************************************

       # Square Free Numbers : These are those numbers which are not divisible by any perfect square , i.e. , "Free of (Perfect) Squares".
            Example  >>> N = 20
              Factors =  2, 4, 5, 10, 20

                 In here, 4 and 20 are divisible by their $ which is a Perfect Square, so they aren't Square Free.
                 on the other hand,  2, 5, and 10 don't have any factor which is a Prefect Square, so they are Square Free.
                 
*******************************************************************************************************************************************************'''                 

                            # Can Use "return" keyword 2 or more times
def test(a):
    if a == 5:
        return 1
    else:
        return 0

N = int(input())
print(test(N))

                            # Can Compare "datetype(s)" of values
a=5.6
b=6.9
if type(a) == type(b):
    print("1")
else:
    print("0")

print(type(14.9))

                            # Trick To Check Whether The No. Is Perfect Square Or Not
import math

def chk_sqy(s):
    flag = 0
    for i in range(2,s//2 + 1):
        if s/i == math.sqrt(s):
            flag = 1
            break
    if flag == 1:
        chk = 1
    else:
        chk = 0

    return chk

n = int(input())
if chk_sqy(n) == 1:
    print('Yes')
else:
    print("No")


                            # Python File Handling
                            
f = open("pythonfile.txt","w+")
for i in range(10):
    f.write("This is line %d\n " %(i+1) )
f.close

f = open("pythonfile.txt","a+")
for i in range(2):
    f.write("Appended line %d\n" %(i+1) )
f.close()

#f = open("pythonfile.txt","r")
with open("pythonfile.txt") as f:  # Alternative way of 'opining' a file, 'cause it automaticlly closes the file at the end of the program so we need not to write "f.close()" at the end.
        while f.read(1):  # Other way to read till EOF is [ while f.read() == '': ]  
            print(f.read())
f.close()

f = open("pythonfile.txt")
flag = 0
c = f.readlines()
print("\n\tt=",c[5])
print("\n\tj=",len(c[5]))                        


                            # Sorting Algo [*works only when the length of list is equal to the largest no. present in the list]

a = [3,6,5,4,1,2]
for i in range(len(a)):
    print(a)
    j = a[i] - 1
    a[i], a[j] = a[j], a[i]
print(a)
                        
                            # Dictionary
                            
d = {}
a = ["Mohit","Mummy","Papa","Muskan"]
for i in range(len(a)):
    d[i+1] = a[i]
print(a)
print(d)
                            
''' Cmd Prompt Trick:
   ******************
           1) Add "/q" or "/Q" after "del" command to ignore or skip the message :-

                " Are You Sure (Y/N)? "
                
            If we use "/q" then cmd prompt will not ask question.

           2) To skip the message "Are You Sure (Y/N)?" in "CACLS" command use "echo" command :-

                " echo Y| cacls folder_name /p everyone:n "  '''

                            # Using "lambda" Function
a = 5
b = 9
res = lambda m,n : m*n
print(res(2,3))
print(res(a,b))


                            # Using Two Loop Simultaneosuly
a = [1,2,3]
b = [4,5,6]
#for i,j in zip(range(len(a)),range(len(b))):
for i,j in zip(a,b):
    print(f" {i}:{j}")


                            # Using 'f-strings'
i = 2
j = 3
k = 9
c = f"{i}:{j}"
c = c + f":{6}"
print(c)

c = []
i = 0
j = 'k'
c.append('l')
c.append(f"{i}:{j}")
print(c)

                            # To know how much time is program taking
                            
start_time = time.time()  # Use this line after taking input
print("--- %s seconds ---" %(time.time - start_time) )  # Use this line at the end or inside Loops to know how much time is that loop taking
                            

                            # 'delay()' in Python ( sleep() )
from  time import sleep

a = []
for i in range(3):
    ele = []
    ele = input().split()
    ele = list(map(lambda x: int(x), ele))
    tl = list(map(lambda x: x+1, ele))
    print(tl)
    a.append(ele)

for i in range(3):
    print(end = '\n')
    for j in range(3):
        print(a[i][j], end = ' ')
        #sleep(0.5)
    sleep(0.5)

                            
                            # Get Current Time
import time as timing

t = timing.localtime()
curr_time = timing.strftime("%I:%M %p", t)
print(curr_time)
                            

                            # Can Return [ True] and [ False] Value in a Function
def test(st):
    st = st.split(' ')
    for s in st:
        if s == 'what':
            return True  ## or [ return 1 ] as '1' also serves as 'True'
            break
    else:
        return False     ## or [ return 0 ] as '0' also serves as 'False'


if test('In what temperature'):
    print('Yes')
else:
    print('Shoot')


                            # To check for a String Present in Another String                            
a = ['My name is Singh', 'My name is Khan']
for st in a:
    if 'is Khan' in st:
        print('success')
        print(st)
                            

        
                            
                            # Print and Store "Traceback Error"
import traceback

try:
    a = [1,2,3,4]
    b = 6
    b = a + b
    print(a)
    print(b)
    
#except Exception as e:
except:    
    c = traceback.format_exc()    
    b = a[0] + b +10
    print(a)
    print(b)    
    print('\n\nDisplaying "Traceback" Error:\n\n', c)




                        
