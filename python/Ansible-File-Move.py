from shutil import copyfile
from sys import exit
import os
import shutil

src_host = raw_input('Enter Host to Source: ')
src_file = raw_input('Enter File to Move: ')
src_dir = raw_input('Enter Directory: ')


#Move Ansible Files
dir_src = "/home/dlakey/Auto-Demo/roles/" + src_host + "/" + src_dir + "/" + src_file
#
with open('files/ets-demo-host.txt', 'r') as hostfile:
	for line in hostfile:
		line = line.strip().lower()
		dir_dst = "/home/dlakey/ETS-Demo/roles/" + line + "/" + src_dir + "/" + src_file
		try:
			copyfile(dir_src, dir_dst)
		except IOError as e:
			print("Unable to copy file. %s" %e)
			exit(1)

print("\nFile copy done!\n")


