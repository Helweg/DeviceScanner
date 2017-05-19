# DeviceScanner
## Description:
This project is a combination of an active and passive device scanner, that will determine the IP's and MAC addresses of devices connected to its subnet. It will compare the IP's and MAC's it finds with a predetermined list of allowed devices.
## How to setup the system:
To setup the system, make sure you have a device that can ssh into the remote device using keys. The remote device needs disable the asking of password for sudo, this can be edited with visudo.   

## Elements in the system:
#### List of allowed devices:
/devices/allowedDevices.txt
#### Scanners:
/scanner/activeScan.py   
/scanner/passiveScan.py
#### Service script:
/systemd/deviceScanner.service
#### Ansible playbook and inventory:
/ansible/deployScan.yml   
/ansible/inventory
