import sys
import yaml
import json
from sys import exit
import os
from napalm import get_network_driver
from getpass import getpass
os.linesep

ios_device='172.16.2.31'
ios_user='cisco'
ios_password='cisco'
driver = get_network_driver('ios')
device = driver(ios_device, ios_user, ios_password)
device.open()

print "ARP Table"
arp_table = device.get_arp_table()
print
print 'Arp Table Information'
print(json.dumps(arp_table, sort_keys=True, indent=4))

#for line in arp_table:
	#line = line.strip().lower()
	#print line

bgp_nei = device.get_bgp_neighbors()
print(json.dumps(bgp_nei, sort_keys=True, indent=4))

dev_info = device.get_facts()
print
print 'Device Information'
print(json.dumps(dev_info, sort_keys=True, indent=4))

int_info = device.get_interfaces()
print
print 'Device Interface Information:'
print(json.dumps(int_info, sort_keys=True, indent=4))

for line in bgp_nei:
	#line = line.strip().lower()
	print line

device.close()
