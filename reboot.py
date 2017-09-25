#!/usr/bin/python

import os, time


#print 'It works till this point'
error = 0

for i in range(1,101):
	#dut.reboot()
	dut.setPrompt('#')
	show_output = dut.sendCmd('dir')
	print show_output
        time.sleep(30)
        
	dut.sendCmd('reboot stack-member 3')
	print 'Number of Reboots %d / %d error' % (i,error)
print 'Final Number of Reboots %d / %d error' % (i,error)


#print 'Number of Reboots %d' % (i)
#print 'Final Number of Reboots %d' % (i)

#print 'Number of Reboots %d / %d error' % (i,error)
#print 'FInal Number of Reboots %d / %d error' % (i,error)

#print 'Number of Reboot %d' % (i)
