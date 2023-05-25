#!/bin/bash
./faktorial2.sh 5
vysledky[0]=1
vysledky[3]=6
vysledky[20]=2432902008176640000 


echo "Hranicni hodnoty: " 
for key in "${!vysledky[@]}"; do
	./faktorial2.sh $key
	if [[ $? -eq ${vysledky[$key]} ]]; then
		echo "pass"
	else
		echo "fail"
		./faktorial2.sh $key
		echo "$?"
		cat >> log.txt <<EOF
Fail $key expected: ${vysledky[$key]} result $? 
EOF
	fi 
done

echo -e "\nPerformance"
time  {
for i in {1..1000}; do 
	./faktorial2.sh 20
done
}

function test(){
	if [[ $2 -eq ${vysledky[$key]} ]]; then
                echo "pass"
        else
                echo "fail"
	fi
{
