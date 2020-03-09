from PIL import Image,ImageFilter

# img = Image.open('D:/Image Processing In Python/Pokedex/pikachu.jpg')
# # print(img.format)
# # print(img.size)
# # print(img)
# # print(img.mode)
# filtered_img = img.filter(ImageFilter.BLUR)
# print(filtered_img)
# filtered_img.save("blur.png",'png') #save(filename,file format)
#
# smooth_img = img.filter(ImageFilter.SMOOTH)
# smooth_img.save("smooth.png","png")
#
# # img2 = Image.open('D:/Image Processing In Python/Pokedex/charmander.jpg')
#
# #Converting image formats
# Grey_img = img.convert('L') # L meang Grayscale
# Grey_img.save('grey.png','png')
# #Grey_img.show()
#
# #Rotatting image
# rotated_img = filtered_img.rotate(180)
# rotated_img.save('rotated.png','png')
#
# #Resizing Image
# new_size = (300,300)
# resized_img = filtered_img.resize(new_size)
# resized_img.save('resized.png','png')
#
# #Cropping Image
# box =(100,100,400,400)
# crop_img = filtered_img.crop(box)
# crop_img.save('cropped.png','png')

#Working on Astro.jpg Image
astro = Image.open('D:/Image Processing In Python/astro.jpg')
print(astro.format)

newbox = (400,200)
astro_resize = astro.resize(newbox)
astro_resize.save('thumbnail.jpg')

'''THUMBNAIL METHOD'''
astro.thumbnail(newbox)
astro.save('newthumbnail.jpg')
