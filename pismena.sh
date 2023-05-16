#!/bin/bash
string="ahoj cau slovo pocitac myska nevim" 
rozdel=' ' read -ra rozdeleneSlova <<< "$string"
for i in "${rozdeleneSlova[@]}"
do
	t="${i^}"
	text="$text $(echo $t)"
done

echo $text
