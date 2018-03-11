#-*- coding: utf-8 -*-

import requests, re

class Zimuzu():
	def __init__(self, user, password):
		self.user = user
		self.password = password
		self.session = requests.Session()
		self.login = self.login(user, password)

	def login(self, user, password):
		loginurl='http://www.zimuzu.tv/User/Login/ajaxLogin'
		httphead={
			'Accept':'application/json, text/javascript, */*; q=0.01',
			'Origin':'http://www.zimuzu.tv',
			'X-Requested-With':'XMLHttpRequest',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded',
			}
		data = "account={}&password={}&remember=1".format(user, password)
		return self.session.post(loginurl, httphead, data)

	def get_links_by_show_name(show):
		url_show = "http://www.zimuzu.tv/resource/" + show
		text = self.session.get(url_show).text
		pat_link = re.compile("ed2k[^\"]*")
		links = []
		links = pat_link.findall(text)
		return links

