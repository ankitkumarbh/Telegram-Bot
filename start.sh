#!/bin/bash

filepath="$(realpath $0)"
mypath="$(dirname "$filepath")"
cd $mypath
python3 -m SaitamaRobot
