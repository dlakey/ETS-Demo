import paramiko
import time
import base64

host = raw_input('Enter Device Name: ')

commands = ['show version\n', 'show run\n']

max_buffer = 65535

def clear_buffer(ssh):
	if ssh.recv_ready():
		return ssh.recv(max_buffer)

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
		time.sleep(8)
		output = new_ssh.recv(max_buffer)
		print(output)
		f.write(output)
	new_ssh.close()




