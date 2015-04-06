#!/bin/bash

counter=0

while [ $counter -lt 30 ]
do
	randomString=`head -c 10 /dev/random | base64`
	randomString="${randomString:0:10}"  
	curl -X POST  -H 'Content-Type: application/json'  -d "{\"name\":\"${randomString}\"}"  http://localhost:5000/students/
	counter=$[ $counter + 1 ]
done


