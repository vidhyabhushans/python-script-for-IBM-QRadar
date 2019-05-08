#!/usr/bin/env python
import netmiko
import base64
'''import re2 as re
regex = re.compile('@')
value = regex.split(user)
b = value[0]'''

from netmiko import ConnectHandler

a = base64.b64decode('YWRtaW4=')

sip = sys.argv[1]
cisco = {
   'device_type': 'cisco_asa',
   'host': 'X.X.X.X',
   'username': 'admin',
   'password': a,
        }
net_connect = ConnectHandler(**cisco)
show_commands = ['configure \n' 'set address obj-%s ip-netmask %s/32 \n' 'edit address-group TEST \n' 'set static obj-%s \n' 'top \n' 'commit \n' % (sip,sip,sip)]
output = ''
for cmd in show_commands:
     output += net_connect.send_command(cmd, delay_factor=2)
