import sys
import paramiko
import time
import base64
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree

max_buffer = 90000
def clear_buffer(ssh):
	if ssh.recv_ready():
		return ssh.recv(max_buffer)

pref = raw_input(' Enter 1 for MAC Address Information\n Enter 2 for Network Route Information\n Enter 3 for Switchport Information\n Enter 4 for Device Information\n User Selection: ')

if pref == '1':
	mac = raw_input('Enter MAC Address of Device in xxxx.yyyy.zzzz format: ')
	
	commands = ['show mac addres address ' + mac]
	command2 = ['show ip arp | include ' + mac]
	
	with open('files/ets-mac-info.txt', 'w') as f:
		with open('files/ets-switch.txt', 'r') as etshost:																
			for line in etshost:																											
				line = line = line.strip().lower()																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																													
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
			 	ssh.connect(line, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
			 	time.sleep(1)
			 	for command in commands:
					stdin, stdout, stderr = ssh.exec_command(command)
					mac_out = stdout.channel.recv(8000)
					if mac in mac_out:
						time.sleep(1)
						f.write("\n\n\n" + line + ":\n\n")
						f.write(mac_out)
				ssh.close()
	
		with open('files/ets-router.txt', 'r') as etshost1:																
			for line in etshost1:																											
				line = line = line.strip().lower()																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																													
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
			 	ssh.connect(line, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
			 	time.sleep(1)
			 	for command in command2:
					stdin, stdout, stderr = ssh.exec_command(command)
					mac_arp = stdout.channel.recv(8000)
					if mac in mac_arp:
						time.sleep(1)
						f.write("\n\n\n" + line + ":\n\n")
						f.write(mac_arp)
				ssh.close()

elif pref == '2':
	route = raw_input('Enter IP Route in X.X.X.0 format: ')
	
	commands = ['show ip route ' + route]
	
	with open('files/ets-route-info.txt', 'w') as f:
		with open('files/ets-router.txt', 'r') as etshost:																
			for line in etshost:																											
				line = line = line.strip().lower()																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																													
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
			 	ssh.connect(line, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
			 	time.sleep(1)
			 	for command in commands:
					stdin, stdout, stderr = ssh.exec_command(command)
					ip_route = stdout.channel.recv(8000)
					f.write("\n\n\n\n" + line + " Router:\n\n")
					f.write(ip_route)
					
				ssh.close()
elif pref == '3':
	host = raw_input('Enter Switch Name: ')
	sw_intf = raw_input('Enter Switch Interface in giX/Y format: ')
	
	commands = ['show int ' + sw_intf + ' switchport', 'show int ' + sw_intf + ' controller', 'show policy-map int ' + sw_intf]

	with open('files/'+ host + '-switchport-info.txt', 'w') as f:
		f.write("\n\n Switch: " + host + "\n")
		for command in commands:																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																													
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
			ssh.connect(host, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
			time.sleep(1)
			stdin, stdout, stderr = ssh.exec_command(command)
			time.sleep(4)
			intf = stdout.channel.recv(8000)
			f.write("\n'\n")
			f.write(intf)
			ssh.close()

elif pref == '4':
	host = raw_input('Enter Device Name: ')
	commands = ['show version\n', 'show config\n', 'show logging\n']
	with open('files/' + host + '-info.txt', 'w') as f:																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
		ssh.connect(host, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
		new_ssh = ssh.invoke_shell()
		output = clear_buffer(new_ssh)
		time.sleep(1)
		new_ssh.send("terminal length 0\n")
		output = clear_buffer(new_ssh)
		for command in commands:
			new_ssh.send(command)
			time.sleep(10)
			output = new_ssh.recv(max_buffer)
			f.write(output)
		new_ssh.close()

else:
   print 'You entered an incorrect value, program will now close'
   dev.close()




