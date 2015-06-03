from PIL import Image

def RGB2BlackWhite(filename):  
    im=Image.open(filename)  
    print "image info,",im.format,im.mode,im.size  
    (w,h)=im.size  
    R=0  
    G=0  
    B=0  
  
    for x in xrange(w):  
        for y in xrange(h):  
            pos=(x,y)  
            rgb=im.getpixel( pos )  
            (r,g,b)=rgb  
            R=R+r  
            G=G+g  
            B=B+b  
  
    rate1=R*1000/(R+G+B)  
    rate2=G*1000/(R+G+B)  
    rate3=B*1000/(R+G+B)  
    print R+G+B
      
    print "rate:",rate1,rate2,rate3  
  
      
    for x in xrange(w):  
        for y in xrange(h):  
            pos=(x,y)  
            rgb=im.getpixel( pos )  
            (r,g,b)=rgb  
            n= r*rate1/1000 + g*rate2/1000 + b*rate3/1000  
            #print "n:",n  
            if n>=200:  
                im.putpixel( pos,(255,255,255))  
            else:  
                im.putpixel( pos,(0,0,0))  
                  
    im.save("2.jpg")  

def removeDot(filename):
    image=Image.open(filename)
    pixdata = image.load()
    print pixdata[0, 0]
    print pixdata[1, 0]
    print pixdata[2, 0]
    m = image.size[1]
    n = image.size[0]
    pix = [None] * m
    for i in range(len(pix)):
        pix[i] = [0] * n
    print (m, n)

    for x in xrange(m):
        for y in xrange(n):
            if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                pix[x][y] = 8
            else:
                sum = 0
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if i == x and j == y:
                            break
                        if pixdata[y, x] != pixdata[j, i]:
                            sum += 1
                pix[x][y] = sum
    for x in xrange(m):
        for y in xrange(n):
            if pix[x][y] > 5:
                pixdata[y, x] = (255, 255, 255)
    image.save('3.jpg')



                  
if __name__=="__main__":    
    RGB2BlackWhite('1.jpg')
    removeDot('2.jpg')  