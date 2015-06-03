from blwh import *
from open import *
from crop import *
from knn import *

import cStringIO
import requests
import random
import time
ipPoor = []

def makeIP():
	global ipPoor
	for i in range(56,243):
		ipPoor.append('60.13.154.' + str(i))
		ipPoor.append('60.13.183.' + str(i))
		ipPoor.append('60.13.148.' + str(i))
		ipPoor.append('60.13.212.' + str(i))
		ipPoor.append('60.13.192.' + str(i))
		ipPoor.append('61.233.202.' + str(i))

if __name__ == '__main__':
	makeIP()
	createDataSet()
	for i in range(1,10000):
		try:
			t = random.randint(4, 10)
			if i % 50 == 0:
				t = 15
			print t
			r = requests.get('http://vote.moveredu.com')
			cookies = dict(r.cookies)
			ip = ipPoor[random.randint(0,1120)]
			headers={"X-Forwarded-For":ip,
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate, sdch",
			"Accept-Language":"zh-CN,zh;q=0.8",
			"Connection":"keep-alive",
			"Host":"vote.moveredu.com",
			"Referer":"http://vote.moveredu.com/index.asp",
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"}
			imageHeaders={"X-Forwarded-For":ip,
			"Accept":"image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate, sdch",
			"Accept-Language":"zh-CN,zh;q=0.8",
			"Cache-Control":"max-age=0",
			"Connection":"keep-alive",
			"Host":"vote.moveredu.com",
			"Referer":"http://vote.moveredu.com/yzm.asp?id=49",
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"}
			resultHeaders = {"X-Forwarded-For":ip,
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate",
			"Accept-Language":"zh-CN,zh;q=0.8",
			"Cache-Control":"max-age=0",
			"Connection":"keep-alive",
			"Content-Length":"51",
			"Content-Type":"application/x-www-form-urlencoded",
			"Host":"vote.moveredu.com",
			"Origin":"http://vote.moveredu.com",
			"Referer":"http://vote.moveredu.com/yzm.asp?id=49",
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"}
			s1 = requests.get('http://vote.moveredu.com/yzm.asp?id=49', headers=headers, cookies=cookies)
			s2 = requests.get('http://vote.moveredu.com/aspyzm/code_25.asp', headers=imageHeaders, cookies=cookies)
			im = Image.open(cStringIO.StringIO(s2.content))
			im.save('1.bmp')
			huidu('1.bmp')
			erzhi('l.jpg')
			quzao('bw.jpg')  
			quzao('wb.jpg')
			quzao('wb.jpg')
			quzao('wb.jpg')
			cropImage()
			result = getResult()
			data = {'CheckCode': str(result), 'pid': '49'}
			time.sleep(1)
			s3 = requests.post('http://vote.moveredu.com/vote2.asp', headers=resultHeaders, cookies=cookies, data=data)

		except Exception as e:
			print e
			continue
