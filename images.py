from PIL import Image,ImageFilter

img = Image.open('D:/Image Processing In Python/Pokedex/pikachu.jpg')
# print(img.format)
# print(img.size)
# print(img)
# print(img.mode)
filtered_img = img.filter(ImageFilter.BLUR)
print(filtered_img)
filtered_img.save("blur.png",'png') #save(filename,file format)

smooth_img = img.filter(ImageFilter.SMOOTH)
smooth_img.save("smooth.png","png")

# img2 = Image.open('D:/Image Processing In Python/Pokedex/charmander.jpg')

#Converting image formats
Grey_img = img.convert('L') # L meang Grayscale
Grey_img.save('grey.png','png')
Grey_img.show()