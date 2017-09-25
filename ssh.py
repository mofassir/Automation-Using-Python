import pexpect
import sys
import datetime
import os

switch_ip = "192.168.1.100"
switch_un = "manager"
switch_pw = "friend"
switch_enable_pw = "m0r3s3cr3t"
port = "Gi2/0/2"
vlan = 300


child = pexpect.spawn('sudo ssh %s@%s' % (switch_un, switch_ip))
child.logfile = sys.stdout
#child.expect('Are you sure you want to continue connecting (yes/no)?')
#child.sendline("yes")
#child.expect('testing new message for user')
child.expect('Password: ')
child.sendline(switch_pw)
child.expect('>')
child.sendline("enable")
child.expect('#')
child.sendline("show ssh server")
child.expect('#')
child.sendline("show users")
child.expect('#')
child.sendline("exit")



newruntime = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%H:%M %d.%m.%Y")
command = 'echo " python ssh.py" | at ' + newruntime
os.system(command)
