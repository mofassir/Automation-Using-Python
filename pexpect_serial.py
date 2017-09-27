import serial
import pexpect
import sys
import datetime
import os
import time 


switch_ip = "192.168.1.100"
switch_un = "manager"
switch_pw = "friend"

child = pexpect.spawn ('sudo minicom s0')

child.logfile = sys.stdout

child.sendline("\n")

child.expect('TOE ')
child.sendline(switch_un)
child.expect('Password: ')
child.sendline(switch_pw)
child.expect('>')
child.sendline("enable")
child.expect('#')
child.sendline("show ssh server")
child.expect('#')
