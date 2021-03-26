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

