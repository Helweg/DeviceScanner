# DeviceScanner
## Description:
This project is a combination of an active and passive device scanner, that will determine the IP's and MAC addresses of devices connected to its subnet. It will compare the IP's and MAC's it finds with a predetermined list of allowed devices.
## To install:
1. Clone repo
2. Copy the /devices/ and the /scanner/ directories to /opt/deviceScanner/
3. Copy /systemd/deviceScanner.service to /lib/systemd/system/
4. Make the deviceScanner.service executable with: chmod 644 /lib/systemd/system/deviceScanner.service
5. Enable service with: systemctl enable deviceScanner.service
6. Reload the services with: systemctl daemon-reload
7. Start the services with: systemctl start deviceScanner.service
8. Test if the service is running with: systemctl status deviceScanner.service

## Elements in the system:
#### List of allowed devices:
/devices/allowedDevices.txt
#### Scanners:
/scanner/activeScan.py   
/scanner/passiveScan.py
#### Service script:
/systemd/deviceScanner.service
