#!/usr/bin/python

# Python file to retrive username/password and cookie from Login HTML page/form and pass it to REST API 


import cgi

form=cgi.FieldStorage()
username_rx = form['username_form'].value
password_rx = form['password_form'].value
cookie_rx = form['cookie_form'].value



import requests
pload = {'username':username_rx,'password':password_rx}
headers = {'Accept':'application/json','Cookie':cookie_rx,'Content-Type':'application/x-www-form-urlencoded,application/json;charset=utf-8','Accept-Encoding':'gzip, deflate, br', 'Connection':'keep-alive'}
r = requests.post('https://xxxxxxxxxxxxxxxxxx/xxxxxxx/rest/v1.0/login',data = pload, headers = headers)
print(r.text)
