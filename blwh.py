from PIL import Image

def erzhi(filename):
	im = Image.open(filename)
	m = im.size[1]
	n = im.size[0]
	pixdata = im.load()
	threshold = 225
	for x in xrange(m):
		for y in xrange(n):
			if pixdata[y, x] < threshold:
				pixdata[y, x] = 0
			else:
				pixdata[y, x] = 255
	im.save('bw.jpg')

def huidu(filename):
    img = Image.open(filename)
    i = img.convert('L')
    i.save("l.jpg")

if __name__=="__main__":    
    huidu('13.bmp')
    erzhi('l.jpg')