#!/bin/bash

./wordcount.sh "a"
string=$(<log.txt)
if [[ $string  -eq 6 ]];then
	echo "pass"
else
	echo "fail"
fi
