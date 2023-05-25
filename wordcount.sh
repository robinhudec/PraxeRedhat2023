#!/bin/bash
string=$(<text.txt) 

rozdel=' ' read -ra rozdeleneSlova <<< "$string"
declare -i index
index=0

for i in "${rozdeleneSlova[@]}"
do
	if [[ ${i:(-1)} == "." || ${i:(-1)} == "," ]];then
		rozdeleneSlova[$index]="${i::(-1)}"
	elif [[ ${i:(-2):1} == "," ]];then 
	       rozdeleneSlova[$index]="${i::(-2)}"
	fi
	rozdeleneSlova[$index]=${rozdeleneSlova[$index],,}
	index+=1
done


declare -A pocty
pocty["a"]=""
declare -i je

for i in "${rozdeleneSlova[@]}"
do
	je=0 
	for key in "${!pocty[@]}";
	do 
		if [[ $key == $i  ]];then
			je=2
		fi
	done
	if [[ $je -eq 0  ]];then
		pocty[$i]=1
	else
		pocty[$i]+=1
	fi
done

echo "${#pocty[$1]}" >| log.txt

#for key in "${!pocty[@]}"
#do
#	echo "$key"
#	echo "${#pocty[$key]}"
#done
