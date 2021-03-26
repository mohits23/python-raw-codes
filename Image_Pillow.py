from PIL import Image

#Open image using Image module
im = Image.open("F:/myImages/coolCat.jpg")

#Show actual image
im.show()

#Show rotated image
r_im = im.rotate(45)
r_im.show()
