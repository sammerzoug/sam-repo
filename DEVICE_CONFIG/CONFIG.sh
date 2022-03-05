#!/bin/bash

>config

echo "ENTER CONFIGURATION TO THE FILE YES/NO:"
read input
i=$input
while [ $i == yes ]
do
echo "ENTER CONFIGURATION LINE: "
read Conf_line
sleep 2
echo $Conf_line >> config
sleep 2
echo "ENTER CONFIGURATION TO THE FILE YES/NO:"
read input
i=$input
done
#THIS PYTHON SCRIPT DEPLOYS THE CONFIG SAVED WITHIN config file
python3.8 routerscript.py

