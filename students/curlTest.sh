#!/bin/bash

case $1 in
	1)
		echo -e "Testing GET\n"
		curl http://localhost:5000/students/
		echo 
		;;
	2)
		echo -e "What index? : "
		read input
		echo -e "Testing GET\n"
		curl http://localhost:5000/students/${input}
		;;
	3)
		echo -e "Name? : "
		read input
		echo -e "Testing PUT\n"
		curl -X POST  -H 'Content-Type: application/json'  -d "{\"name\":\"${input}\"}"  http://localhost:5000/students/
		;;
	4)
		echo -e "What index? :"
		read input
		echo -e "Change to what name? :"
		read new_name
		echo -e "Testing POST\n"
		curl -X PUT -H 'Content-Type: application/json' -d "{\"name\":\"${new_name}\"}" http://localhost:5000/students/${input}
		;;
	*)
		echo -e "Invalid\n"
		;;	
esac
