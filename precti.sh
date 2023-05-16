#!/bin/bash
function precti(){
	let pocet=1
	while read -r line; do
  		echo "$pocet $line"
  		let pocet++
	done <$1
}

precti soubor.txt

