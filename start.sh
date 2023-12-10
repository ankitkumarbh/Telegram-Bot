#!/bin/bash

filepath="$(realpath $0)"
mypath="$(dirname "$filepath")"
cd $mypath
pip install telethon -U
python3 -m SaitamaRobot
