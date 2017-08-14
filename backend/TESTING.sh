#!/bin/bash
cmdpid="" 

file="data.db"


tester () {

sleep 3
pyresttest http://127.0.0.1:5000 tests/auth.yaml --log debug
kill $cmdpid 
}

server () {

    cmd= python app.py
    $cmd& cmdpid=$!
    
}

echo "Removing data.db"
if [ -f $file ] ; then
    rm $file
fi

tester & server

