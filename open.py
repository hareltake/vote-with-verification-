from PIL import Image

def  Corrode(filename):
	im = Image.open(filename)
	m = im.size[1]
	n = im.size[0]
	pixdata = im.load()
	kH = range(2)+range(n-2,n)
	kW = range(2)+range(m-2,m)
	for i in range(m):
		for j in range(n):
		    if i in kW or j in kH:
		        pixdata[j, i] = 255
		    elif pixdata[j, i] == 255:
		        pixdata[j, i] = 255
		    else:
		        a = []
		        for k in range(5):
		            for l in range(5):
		                a.append(pixdata[j-2+l, i-2+k])
		        if max(a) == 255:
		            pixdata[j, i] = 255
		        else:
		            pixdata[j, i] = 0
	im.save('bw.jpg')

def Expand(filename):
    im = Image.open(filename)
    m = im.size[1]
    n = im.size[0]
    pixdata = im.load()

    pix = [None] * m
    for i in range(len(pix)):
        pix[i] = [0] * n

    for i in range(m):
        for j in range(n):
            if pixdata[j, i] == 0:
            	pix[i][j] = 1
    for i in range(m):
        for j in range(n):
            if pix[i][j] == 1:
                for k in range(5):
                    for l in range(5):
                        if -1<(i-2+k)<m and -1<(j-2+l)<n:
                            pixdata[j-2+l, i-2+k] = 0
    im.save('bw.jpg')

def quzao(filename):
	im = Image.open(filename)
	m = im.size[1]
	n = im.size[0]
	pixdata = im.load()

	pix = [None] * m
	for i in range(len(pix)):
	    pix[i] = [0] * n

	for i in xrange(m):
		for j in xrange(n):
			if i == 0 or j == 0 or i == m - 1 or j == n - 1:
				pixdata[j, i] = 255
				continue
			if pixdata[j, i] > 120:
				white = 0
				if pixdata[j, i-1] < 120:
					white += 1
				if pixdata[j, i+1] < 120:
					white += 1
				if pixdata[j-1, i] < 120:
					white += 1
				if pixdata[j+1, i] < 120:
					white += 1
				if white > 2:
					pix[i][j] = 1
			elif pixdata[j, i] < 120:
				black = 0
				if pixdata[j, i-1] > 120:
					black += 1
				if pixdata[j, i+1] > 120:
					black += 1
				if pixdata[j-1, i] > 120:
					black += 1
				if pixdata[j+1, i] > 120:
					black += 1
				if black > 2:
					pix[i][j] = 1
	for i in xrange(m):
		for j in xrange(n):
			if pix[i][j] == 1:
				if pixdata[j, i] > 120:
					pixdata[j, i] = 0
				else:
					pixdata[j, i] = 255
	im.save('wb.jpg')


if __name__=="__main__": 
	quzao('bw.jpg')  
	quzao('wb.jpg')
	quzao('wb.jpg')
	quzao('wb.jpg')
