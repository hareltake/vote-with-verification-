import requests
import random
import time

for i in range(1,1000):
	try:
		r = requests.get('http://vote.moveredu.com')
		cookies = dict(r.cookies)
		a = random.randint(1,255)
		b = random.randint(0,255)
		c = random.randint(0,255)
		d = random.randint(0,255)
		ipAddress = "%d.%d.%d.%d" % (a,b,c,d)
		headers={"X-Forwarded-For":ipAddress,
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, sdch",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Connection":"keep-alive",
		"Host":"vote.moveredu.com",
		"Referer":"http://vote.moveredu.com/index.asp",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"}
		s=requests.get('http://vote.moveredu.com/yzm.asp?id=1', headers=headers, cookies=cookies)
		t = random.randint(1,2)
		print t
		time.sleep(t)
		#1842 1690 1120 1386
		# r = requests.get('http://today.hit.edu.cn/commend/112793_1.htm', headers=headers)
	except Exception as e:
		print e
		continue

