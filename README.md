# DeviceScanner
## Description:
This project is a combination of an active and passive device scanner, that will determine the IP's and MAC addresses of devices connected to its subnet. It will compare the IP's and MAC's it finds with a predetermined list of allowed devices.
## Elements in the system:
#### Scanners:
/opt/scanner/activeScan.py
/opt/scanner/passiveScan.py
#### Pressistans script:
/etc/init.d/pressActive.sh
#### Ansible playbook:
/opt/ansible/deployScan.yml
