# DeviceScanner
## Description:
This project is a combination of an active and passive device scanner, that will determine the IP's and MAC addresses of devices connected to its subnet. It will compare the IP's and MAC's it finds with a predetermined list of allowed devices.
## How to setup the system:
## Elements in the system:
#### List of allowed devices:
/opt/devices/allowedDevices.txt
#### Scanners:
/opt/scanner/activeScan.py   
/opt/scanner/passiveScan.py
#### Shell script:
/opt/shellScript/deviceScanner.sh
#### Pressistans script:
/etc/init.d/pressScanner
#### Ansible playbook:
/opt/ansible/deployScan.yml
