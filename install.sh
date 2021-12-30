#!/bin/bash

echo "----------------------------"
echo "this is update / install script v1 for KaliTools"
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
rm update.py
wget https://raw.githubusercontent.com/Rafidaone/KaliTools/main/update.py
echo "---------------------------"
echo "finished task now exiting"
exit

