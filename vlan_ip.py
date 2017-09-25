out=open('vlan_ip.scp','w') 

a = 1

b = 1

first_part = 'ip address 193.'

last_part = '.1/24'



index=1 
for vlan in range(1000,1129): 
	out.write('interface vlan%d\n'%vlan) 

        out.write(first_part+str(a)+'.'+str(index)+last_part)
		                
				
	out.write('\n')

	index+=1

	if index == 255:
		a+=1
		index=1
	 

out.write('exit\n') 
out.close() 
