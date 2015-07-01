import requests
import random
import time

for i in range(1,10):
	try:
		a = random.randint(1,255)
		b = random.randint(0,255)
		c = random.randint(0,255)
		d = random.randint(0,255)
		ipAddress = "%d.%d.%d.%d" % (a,b,c,d)
		headers={"X-Forwarded-For":ipAddress,
		"Accept":"application/json, text/javascript, */*; q=0.01",
		"Accept-Encoding":"gzip, deflate, sdch",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Connection":"keep-alive",
		"Host":"t.hmswhh.com:8081",
		"Referer":"http://t.hmswhh.com:8081/?sortid=2&type=page&id=2534",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
		"X-Requested-With":"XMLHttpRequest"}
		s=requests.get('http://t.hmswhh.com:8081/common/vote.aspx?action=vote&aid=1&pid=2534', headers=headers)
		print s.status_code
		t = random.randint(3,4)
		time.sleep(t)
		#1842 1690 1120 1386
		# r = requests.get('http://today.hit.edu.cn/commend/112793_1.htm', headers=headers)
	except Exception as e:
		print e
		continue

