import paramiko
import time
import base64

def clear_buffer(device):
	if device.recv_ready():
		return device.recv(5000)

commands = ['show version\n']

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('172.16.2.31', username='cisco', password='cisco', look_for_keys=False, allow_agent=False)

new_connection = connection.invoke_shell()
output = clear_buffer(new_connection)
time.sleep(2)
new_connection.send('terminal length 0\n')
output = clear_buffer(new_connection)

for command in commands:
    new_connection.send(commands)
    time.sleep(5)
    device = new_connection.recv(5000)
    print(device)


