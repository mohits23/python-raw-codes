
            ##
a = 'what?'

print(a)

a = a[len(a)-1:len(a)]

print(a)





            ##
import os
import subprocess

command = 'cmd'

os.system(command)

#  [OR]

#subprocess.Popen(command)


# command1 = r'cd C:\Users\Acer\AppData\Local\Programs\Python\Python38-32'
# os.system(command1)
# os.system(r'py C:\Users\Acer\AppData\Local\Programs\Python\Python38-32 hye.py')





            ##
import subprocess

subprocess.call(["gcc", "hello.c"])
subprocess.call("./a.exe");





            ##
import subprocess

print('Started...')

try:
    subprocess.call(["gcc", "hello.c"]) # This Will Compile The 'C' Code and
                                        #  will also return Compile Time Errors.
                                        
    subprocess.call("./a.exe") # This Will Run The 'C' Code and
                               #  will also return Output if No Compile Time
                               # Error is found.
    
except Exception as e:
    print('Console Error :', e)

finally:
    print('Done...!!')






            ##
a = 'a'
b = []

if type(a) == str and type(b) == list:
    print(type(a))
    print(type(b))
else:
    print('Types Not Matched!')






            ##
try:
    a = [1,2,3,4]
    b = 6
    b = a + b
    print(a)
    print(b)
    
except Exception as e:
    #print("Error:", e)
    err = e
    print("Error err:",err)
    b = a[0] + b +10
    print(a)
    print(b)
    print(e)









            ##
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






            ##
 # Converting "array" and "dictionary" into [ "type(str)" ]
    
d = {1:'a', 2:'b', 3:'c', 4:'d'}
a = [1,2,3,4]
#for i in range(1, len(d)+1):
    #print(d[i])
print(d)
print(type(d))

f = str(d)
print(f[3:])
print(type(f))

print(a)
print(type(a))

f = str(a)
print(f[5:])
print(type(f))
    








            ##

import numpy as np
from PIL import Image

image = Image.open('F:/myImages/MohitWall.png')
#image.show()

arr = np.array(image)


print(arr.shape)
print(arr)

count = 0
for x in range(1350):
    for y in range(629):        
        if y == 0:
            arr[y,x] = 255
        else:
            arr[y,x] = 255

print(count)

newImg = Image.fromarray(arr)
newImg.show()




            ##
import numpy as np
from PIL import Image

arr = np.zeros([3400,3400], dtype=np.uint8)

#img = Image.open('F:/myImages/coolCat.jpg')
#arr = np.array(img)

print(arr.shape)

for i in range(3400):
    for j in range(3400):
        if j+i < 2:
            arr[i,j] = 300
        elif i+j > 2:
            arr[i,j] = 100
        elif i+j == 2:
            arr[i,j] = 0

image = Image.fromarray(arr)
image.show()
image.save('F:/myImages/MyBetaWall.png')




