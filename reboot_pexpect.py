import pexpect
import sys
import datetime
import os
import time 


switch_ip = "192.168.1.100"
switch_un = "manager"
switch_pw = "friend"


for i in range(2):

	child = pexpect.spawn('sudo ssh %s@%s' % (switch_un, switch_ip))
	child.logfile = sys.stdout
	child.expect('Password: ')
	child.sendline(switch_pw)
	child.expect('>')
	child.sendline("enable")
	child.expect('#')
	child.sendline("show ssh server")
	child.expect('#')
	child.sendline("show users")
	child.expect('#')
	child.sendline("reboot")
  child.expect('reboot')
  child.sendline("y")
  time.sleep(200)
