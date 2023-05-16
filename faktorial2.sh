#!/bin/bash
function faktorial(){
        if [[ -z $1 ]]; then
                echo "prazdny string"
      	else
                let cislo=0
		let zaklad=1
		for (( i=1 ; i<=$1 ; i++)) ; do
			let cislo++
			let zaklad=$zaklad*$cislo
                        echo $zaklad
                done
        fi
}

faktorial 5



