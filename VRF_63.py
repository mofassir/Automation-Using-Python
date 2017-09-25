import os,time


for x in range (100,163):
    string_info = '.test1.com 192.168.'+str(x)+'.2' 

    for i in range(0,1000):
      lookup_string = 'nslookup '+ str(i) + string_info
      print lookup_string
      #os.system(lookup_string)
      time.sleep(0.15)
