#!/bin/bash
function vypis(){
	cd $1
	ls -p | grep -v / > $2
}

vypis . soubor3.txt
#s1 adresar kam ulozit s2 soubor do ktereho ulozit
