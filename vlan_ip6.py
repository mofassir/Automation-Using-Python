out=open('vlan_ip6.scp','w') 

a = 1

b = 1

first_part = 'ipv6 address 2001:db8:'

last_part = '::1/64'

router = 'ipv6 router ospf area 0'

index=1 
for vlan in range(100,357): 
	out.write('interface vlan%d\n'%vlan) 

        out.write(first_part+str(index)+last_part)
		                
				
	out.write('\n')

        out.write(router)

	
	out.write('\n')
	
	index+=1

	#if index == 255:
	#	a+=1
	#	index=1
	 

out.write('exit\n') 
out.close() 
