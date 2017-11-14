import sys
import paramiko
import time
import base64
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree

pref = raw_input('Enter 1 for MAC Address Information, Enter 2 for Network Route Information, Enter 3 Switchport Power Information, or enter 4 for Router Configuration: ')

if pref == '1':
	mac = raw_input('Enter MAC Address of Device: ')
	
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
   lpref = 'TE_ABOVE_PNI'
elif pref == '3':
   lpref = 'AS_TE_DEPREF'
elif pref == '4':
   lpref = 'AS_TE_ABOVE_PNI'
else:
   print 'You entered an incorrect value, program will now close'
   dev.close()




