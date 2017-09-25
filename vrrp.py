out=open('vrrp_switch.scp','w') 

out.write('enable')

out.write('\n')

out.write('configure terminal')

out.write('\n')


a = 1
b = 1


index=1 
for i in range(1,257): 
	#out.write('interface vlan%d\n'%vlan) 

        out.write('router vrrp %d vlan1' % i)
		                
				
	out.write('\n')

for p in range(1,257):
        #out.write('interface vlan%d\n'%vlan) 

	out.write('router vrrp %d vlan2' % p)


        out.write('\n')

for m in range(1,257):
        #out.write('interface vlan%d\n'%vlan) 

	out.write('router vrrp %d vlan3' % m)


        out.write('\n')

out.write('exit\n') 
out.close() 
