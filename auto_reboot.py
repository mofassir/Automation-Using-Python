#!/usr/bin/python
import os, time

error = 0

for i in range(0,1000):
	dut.reboot()
	dut.setPrompt('#')
	show_output = dut.sendCmd('show post | include Image')
	print show_output
        show_output = dut.sendCmd('show process | include rng')
	print show_output
        time.sleep(0)
        print 'Number of Reboots %d / %d error' % (i,error)
print 'Final Number of Reboots %d / %d error' % (i,error)
#print 'Number of Reboot %d' % (i)
