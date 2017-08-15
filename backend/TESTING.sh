#!/bin/bash

file="data.db"


tester () {

sleep 3
pyresttest http://127.0.0.1:5000 tests/all.yaml --log debug
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

