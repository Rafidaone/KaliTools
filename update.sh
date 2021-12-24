#!/bin/bash

clear
echo "this is update / install script for KaliTools"
sleep 0.5
echo ""
read -p "press enter to start update/install press ^C to cancel"
echo ""

pip install colorama
pip install PyAutoGUI

sudo apt install tshark -y
sudo apt install aircrack-ng -y
sudo apt install wifite -y
sudo apt install hashcat -y

rm tools.py
wget https://raw.githubusercontent.com/Rafidaone/KaliTools/main/tools.py

exit

