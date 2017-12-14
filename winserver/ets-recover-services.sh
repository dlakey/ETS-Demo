#!/bin/bash

echo -n "Do you wish to Recover IIS service on sss-win2012-srv1, Enter Yes or No? "
read preply

if [ "$preply" == "Yes" ]
	then
		ansible-playbook --limit "sss-win2012-srv1" -i hosts.bak ets-www-ps.yml
fi

echo -n "Do you wish to Recover DNS service on sss-win2012-srv1, Enter Yes or No? "
read preply

if [ "$preply" == "Yes" ]
	then
		ansible-playbook --limit "sss-win2012-srv1" -i hosts.bak ets-dns-ps.yml
fi