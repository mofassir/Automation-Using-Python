import os,time 

for x in range (102,103):
    string_info = '.test.com 192.168.'+str(x)+'.2'


    for i in range(1,60000):
	lookup_string = 'nslookup '+ str(i) + string_info
	print lookup_string
	os.system(lookup_string)
	time.sleep(0.5)
