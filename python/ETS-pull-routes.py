import sys
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree
from jnpr.junos.utils.config import Config

Host = raw_input('Enter Hostname or IP address of Device: ')
dev = Device(host=Host,user='root',password='Juniper').open()

Peer = raw_input('Enter Peering Device: ')

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

route_table = RouteTable(dev)

route_table.get(protocol='bgp')

for key in route_table:
    if key.nexthop == Peer:
       print key.name + 'Nexthop: ' + key.nexthop + 'Via: ' + key.via + ' Protocol: ' + key.protocol

Continue = raw_input('Do you wish to pull route(s), Yes or No: ')

if Continue == 'Yes':
   proute = raw_input('Enter route to pull in format X.X.X.X/X: ')
   prefix = raw_input('Enter Vendor Prefix: ')
   ticket = raw_input('Enter Ticket Number: ')
else:
   dev.close()

dev.bind(cu=Config)
dev.cu
from lxml import etree

PPolicy = "set policy-options prefix-list " + ticket + ' ' + proute
result = dev.cu.load(PPolicy)
# etree.dump(result)

while Continue == 'Yes':
    Continue = raw_input('Pull more route(s), Yes or No: ')

    if Continue == 'Yes':
      proute = raw_input('Enter route to pull in format X.X.X.X/X: ')
      PPolicy = "set policy-options prefix-list " + ticket + ' ' + proute
      result = dev.cu.load(PPolicy)
#      etree.dump(result)
    else:
      Continue = 'No'

pref = raw_input('Enter 1 for PREFIX_TE_DEPREF, enter 2 for TE_ABOVE_PNI, enter 3 for AS_TE_DEPREF, or enter 4 for AS_TE_ABOVE_PNI: ')

if pref == '1':
   localpref = 'PREFIX_TE_DEPREF'
elif pref == '2':
   localpref = 'TE_ABOVE_PNI'
elif pref == '3':
   localpref = 'AS_TE_DEPREF'
elif pref == '4':
   localpref = 'AS_TE_ABOVE_PNI'
else:
   print 'You entered an incorrect value, program will now close'
   dev.close()

PPolicy = "set policy-options policy-statement IMPORT_FROM_" + prefix + " term " + localpref + " from prefix-list " + ticket
result = dev.cu.load(PPolicy)
# etree.dump(result)

dev.cu.commit(comment= 'INTTEST')
