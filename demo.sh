#!/bin/bash
rpm -q $1
if  [[ $? -gt 0 ]];
then
	sudo dnf install $1
else
	sudo dnf remove $1
fi

rpm -q $1
