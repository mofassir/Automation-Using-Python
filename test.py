#!/usr/bin/python
import time, os, re

device.setPrompt('#')

string_info = 'nslookup 1.mof.com 10.37.52.2'

errorCount = 0

for i in range( 0, 500):
  device.setPrompt('#')
  device.reboot(debug=True)
  device.setPrompt('#')
  device.sendCmd('clear log')
  os.system(string_info)
  time.sleep(3)
  device.sendCmd('show ip dns forwarding cache')
  output = device.sendCmd('show log')
  output
  if output.count('failed') >= 1:
    print '!!!! Issue reproduced'
    errorCount += 1
  else:
    print '>>>> No issue found'
  
  print 'Iteration %d / %d error' % (i,errorCount)
  print '=========================='
  
  
  
