#!/bin/bash
./faktorial2.sh 5
declare -A vysledky
vysledky[5]=120
vysledky[0]=1
vysledky[21]=51090942171709440000

echo "Hranicni hodnoty: " 
for key in "${!vysledky[@]}"; do
	./faktorial2.sh $key
	if [[ $? -eq ${vysledky[$key]} ]]; then
		echo "pass"
	else
		echo "fail"
		./faktorial2.sh $key
		cat > log.txt <<EOF
Fail $key expected: ${vysledky[$key]} result $? 
EOF
	fi 
done

echo -e "\nPerformance"
time {
for i in {1..1000}; do 
	./faktorial2.sh 20
done
}

