#!/usr/bin/python
import os, time
error = 0

for i in range(0,10):
	dut.setPrompt('#')
	dut.sendCmd('configure terminal')
	dut.sendCmd('ip dns forwarding')
	dut.sendCmd('ip dns forwarding cache size 10')
	dut.sendCmd('ip name-server 10.37.52.33')
	dut.sendCmd('exit')
	dut.sendCmd('write')
	time.sleep(3)
	#show = dut.sendCmd('show run')
	#print show
	os.system('nslookup mof.com 10.37.52.2')
  os.system('nslookup 1.mof.com 10.37.52.2')
	result = dut.sendCmd('show ip dns forwarding cache | grep -c mof')
  print type(result)
	print result
	if result.count('2') == 1:
	  print 'Problem Not Detected'
	else:
	  print 'Problem Detected'
	  error +=1
	dut.sendCmd('configure terminal')
	dut.sendCmd('no ip dns forwarding')
	dut.sendCmd('no ip name-server 10.37.52.33')
	dut.sendCmd('exit')
	dut.sendCmd('write')
	#show_again = dut.sendCmd('show run')
	#print show_again
        time.sleep(3)
	dut.reboot()
print 'Number of Reboot %d / %d error' % (i,error)
