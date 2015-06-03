from PIL import Image

#20 40 60 80 100
def cropImage():
	im = Image.open('wb.jpg')

	region1 = (0, 0, 20, 20)
	region2 = (20, 0, 40, 20)
	region3 = (40, 0, 60, 20)
	region4 = (60, 0, 80, 20)
	region5 = (80, 0, 100, 20)

	crop1 = im.crop(region1)
	crop1.save('crop1.jpg')
	crop2 = im.crop(region2)
	crop2.save('crop2.jpg')
	crop3 = im.crop(region3)
	crop3.save('crop3.jpg')
	crop4 = im.crop(region4)
	crop4.save('crop4.jpg')
	crop5 = im.crop(region5)
	crop5.save('crop5.jpg')

if __name__ == '__main__':
	cropImage()