#!/bin/bash

echo -n "Do you wish to verify server processes, Enter Yes or No? "
read preply

if [ "$preply" == "Yes" ]
	then
		echo -n "Enter Server Name: "
		read sipaddress
		ansible-playbook --limit "$sipaddress" -i hosts.bak ets-process-ps.yml
fi

echo -n "Do you wish to stop a Web Server Services on this server, Enter Yes or No? "
read preply

if [ "$preply" == "Yes" ]
	then
		ansible-playbook --limit "$sipaddress" -i hosts.bak ets-www-stop.yml
fi

echo -n "Do you wish to stop a DNS Services on this server, Enter Yes or No? "
read preply

if [ "$preply" == "Yes" ]
	then
		ansible-playbook --limit "$sipaddress" -i hosts.bak ets-dns-stop.yml
fi