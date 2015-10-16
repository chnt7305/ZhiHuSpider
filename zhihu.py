#-*-coding:utf-8 -*-
import re
import os
import json
import sys
type = sys.getfilesystemencoding()
from WebSpider.get_html import GetHTML

url_0 = "http://www.zhihu.com/question/%i"
url_2 = []
host = "www.zhihu.com"

f = open('config.json')
RangeNum = json.load(f)
ST = int(RangeNum["start"])
ED = int(RangeNum["end"])

for i in range(ST,ED):
	a = url_0 % i
	url_2.append(a)

def ZhuaQu(url,host):
	html = GetHTML(url,host)
	req = re.findall(r'''<a class="zg-anchor-hidden" name="(.*?)"></a>


<div class="zm-votebar">
<button class="up ">
<i class="icon vote-arrow"></i>
<span class="label">赞同</span>
<span class="count">(.*?)</span>''',html)
	
	return req

def Title(url,host):
	html = GetHTML(url,host)
	title = re.findall(r'''<title>

(.*?)

</title>''',html)
	return title[0]
	

file_1 = open('zhihu_zhuaqu.txt','a+')
for url in url_2:
	try:
		title = Title(url,host)
		Req = ZhuaQu(url,host)
		for items in Req:
			if int(items[1]) > 10 :
				print >> file_1,title,items[1],url +"#"+ items[0]
	except:
		pass
		
file_1.close()