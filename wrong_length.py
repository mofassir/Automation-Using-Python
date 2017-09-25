import os,time

from scapy.all import send,conf,sendp,srp1,sniff,Ether,IP,ARP,UDP,BOOTP,DHCP

for x in range (1,10):
    string_info = '.test.com 192.168.'+str(x)+'.2'

    #msg("Sending DHCPDISCOVER packet to discover DHCP servers",2)
    send(IP(src="9.9.9.9",dst="10.37.23.66")/UDP(sport=68,dport=67)/BOOTP(htype=1,hlen=24)/DHCP(options=[("message-type","discover"),"end"]))

    time.sleep(.05);


# for i in range(0,60000)
#	lookup_string = 'nslookup '+ str(i) + string_info
#	print lookup_string
#	os.system(lookup_string)
#	time.sleep(5)
