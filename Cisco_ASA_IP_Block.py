#!/usr/bin/env python
import paramiko, time

host = 'xx.xx.xx.xx'
password = '*******'
username = 'admin'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password)
print('Successfully connected to %s' % host)

remote_conn = ssh.invoke_shell()
output = remote_conn.recv(1000)

# Disable paging on Brocade.
remote_conn.send('terminal length 0\n')
# Check interface status.
remote_conn.send('configure \n')
remote_conn.send('set address obj-1.1.1.20 ip-netmask 1.1.1.20/32 \n')
remote_conn.send('edit address-group TEST \n')
remote_conn.send('set static obj-1.1.1.20 \n')
remote_conn.send('top \n')
remote_conn.send('commit \n')
remote_conn.send('show jobs all\n') # I only want output from this command.

time.sleep(2)
output = remote_conn.recv(5000)
'''print(output)

for line in output.split('\n'):
    if 'line protocol is up' in line:
        print(line)'''
