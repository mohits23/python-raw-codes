
    # Dimension : (Brackets at Beginning/End)
    # Last Value in Dimensions : (Brackets at Beginning/End) - 1



from PIL import Image
from numpy import array

image = Image.open('F:/myImages/coolCat.jpg')
#image.show()

img2arr = array(image)  ## array() is "Numpy" function
print(type(array(image)))

print('\n\t**********************************************')
print(img2arr)
print('\n\t**********************************************')

arr2Image = Image.fromarray(img2arr)  ## fromarray() is from "Pillow"
arr2Image.show()

arr2Image.save("F:/myImages/Array2Image.jpg")
arr2Image.save("F:/myImages/Array2Image.png")



    #########################################################



from PIL import Image
from numpy import array

image = Image.open('F:/myImages/coolCat.jpg')
#image.show()

img2arr = array(image)  ## array() is "Numpy" function
print(type(array(image)))
print(array(image).ndim)
print(img2arr.ndim)


print('\n\t**********************************************')
print(img2arr)
print('\n\t**********************************************')




    ##################################################################





import numpy as np
from PIL import Image

print('\n\t************************************************\n')
arr = np.zeros([1500, 3400, 3], dtype=np.uint8)
print(arr)

print('\n\t************************************************\n')
arr[:, :1500] = [255, 255, 0]
print(arr)

print('\n\t************************************************\n')
arr[:, 1800:] = [0, 255, 255]
print(arr)

print('\n\t************************************************\n')


arr2img = Image.fromarray(arr)
arr2img.show()

arr2img.save('F:/myImages/PixelArt.png')




    ##################################################################




import numpy as np
from PIL import Image

arr = np.zeros([1500, 3000], dtype=np.uint8)

for x in range(3000):
    for y in range(1500):
        if (x%16 // 8) == (y%16 //8):
            arr[y,x] = 255
        else:
            arr[y,x] = 0

arr2img = Image.fromarray(arr)
arr2img.show()

arr2img.save('F:/myImages/Dotted_Pixels.png')







    ############## First Diagonal Two Colour Tone Shade Pixel Image #######


import numpy as np
from PIL import Image

arr = np.zeros([3400,3400], dtype=np.uint8)

#img = Image.open('F:/myImages/coolCat.jpg')
#arr = np.array(img)

print(arr.shape)

for i in range(3400):
    for j in range(3400):
        if j>i:
            arr[i][j] = 100
        elif i>j:
            arr[i][j] = 300
        elif i==j:
            arr[i][j] = 0

image = Image.fromarray(arr)
image.show()
image.save('F:/myImages/MyFirstWall.png')













    ############## Second Diagonal Two Colour Tone Shade Pixel Image #######

import numpy as np
from PIL import Image

arr = np.zeros([3400,3400], dtype=np.uint8)

#img = Image.open('F:/myImages/coolCat.jpg')
#arr = np.array(img)

print(arr.shape)

for i in range(3400):
    for j in range(3400):
        if i+j < 3400:
            arr[i,j] = 300
        elif i+j > 3400:
            arr[i,j] = 100
        elif i==j:
            arr[i,j] = 0

#print(arr)

image = Image.fromarray(arr)
image.show()
image.save('F:/myImages/MyBetaWall.jpg')
