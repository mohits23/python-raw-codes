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
