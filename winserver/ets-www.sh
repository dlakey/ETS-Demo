#!/bin/bash

echo -n "Do you wish to enable IIS service on sss-win2012-srv1, Enter Yes or No? "
read preply

if [ "$preply" == "Yes" ]
	then
		ansible-playbook --limit "sss-win2012-srv1" -i hosts.bak ets-www-ps.yml
fi