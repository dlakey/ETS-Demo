import paramiko
import time
import base64
import sys
import cmd
import json
import yaml
import os

host = raw_input('Enter Hostname or IP address of Device: ')

commands = ['show vlan']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
dev = ssh.invoke_shell()

# Enable Mode
dev.send('enable\n')

#Enable Password
dev.send('cisco\n')
resp = dev.recv(0)

#Turn of Terminal Paging
dev.send('terminal length 0\n')
resp = dev.recv(0)

#Dump Config
dev.send('show run\n')
time.sleep(3)
resp = dev.recv(9999)
counter = 0
with open('../roles/' + host + '/files/' + host + '.cfg', 'w') as f:
	for line in resp:
		if counter < 21:
			counter = counter + 1
			continue
		f.write(line)


	#resp = dev.recv(9999)
	#print resp