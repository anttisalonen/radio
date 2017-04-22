#!/bin/bash

source ~/virtualenv-15.1.0/ve/bin/activate

./run_checker.sh &

while [ 1 ]; do
	FLASK_APP=hello.py flask run --host=0.0.0.0
	sleep 1
done

