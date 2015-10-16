#-*-coding:utf-8 -*-
import urllib
import urllib2
import json
import cookielib

def GetHTML(url,host):
	cookie_jar = cookielib.MozillaCookieJar()
	cookies = open('./WebSpider/cookies.txt').read()
	for cookie in json.loads(cookies):
		cookie_jar.set_cookie(cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False, domain=cookie['domain'], domain_specified=False, domain_initial_dot=False, path=cookie['path'], path_specified=True, secure=cookie['secure'], expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))
	cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
	headers = {
			"GET":url,
			"Host":host,
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
			}
	request = urllib2.Request(url)
	for key in headers:
		request.add_header(key,headers[key])
	opener = urllib2.build_opener(cookie_handler)
	response = opener.open(request)
	page = response.read()
	return page