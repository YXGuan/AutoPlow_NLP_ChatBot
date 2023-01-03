#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1

ls & roscore &  python3 tkinterTest1.py && fg
