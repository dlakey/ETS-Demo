import paramiko
import time
import base64

host = raw_input('Enter Hostname or IP address of Device: ')

commands = ['enable', 'config t', 'license grace', 'exit', 'show feature', 'show license']

with open(host + '_show_cmd.cfg', 'w') as f:
	for command in commands:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	 	ssh.connect(host, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
	 	time.sleep(1)
		stdin, stdout, stderr = ssh.exec_command(command)
		time.sleep(3)
		f.write(stdout.channel.recv(8000))
		ssh.close()



