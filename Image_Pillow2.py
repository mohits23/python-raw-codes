from PIL import Image, ImageDraw

#Open image using Image module
im = Image.open("F:/myImages/coolCat.jpg")

    # Show actual image
#im.show()

    # Show rotated image
#r_im = im.rotate(45)

#r_im.show()
#r_im.save('rotateCat.png')
#r_im.save('F:/myImages/coolCat.gif', 'GIF')


    # Adjusting RGB Configuration of Image
#r, g, b = im.split()
#rgb_Image = Image.merge("RGB", (b, g, r))
#rgb_Image.show()
#rgb_Image.save('F:/myImages/RGB_Cat.png')


img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)

draw.rectangle(
   (200, 125, 300, 200),
   fill=(255, 0, 0),
   outline=(0, 0, 0))
img.show()




print(end='\n')

print(im.size)
print(end='\n')

print(im.height)
print(end='\n')

print(im.info)
print(end='\n')

print(im.palette)
print(end='\n')

print(im.mode)
print(end='\n')
