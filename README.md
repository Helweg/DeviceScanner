# DeviceScanner
## Description:
This project is a combination of an active and passive device scanner, that will determine the IP's and MAC addresses of devices connected to its subnet. It will compare the IP's and MAC's it finds with a predetermined list of allowed devices.
## To install:
1. Clone repo
2. Change the configure file to fit your needs /config/scannerConf.yml
3. Copy the /devices/ and the /scanner/ directories to /opt/deviceScanner/
4. Copy /systemd/deviceScanner.service to /lib/systemd/system/
5. Make the deviceScanner.service executable with: chmod 644 /lib/systemd/system/deviceScanner.service
6. Enable service with: systemctl enable deviceScanner.service
7. Reload the services with: systemctl daemon-reload
8. Start the services with: systemctl start deviceScanner.service
9. Test if the service is running with: systemctl status deviceScanner.service

## Elements in the system:
#### List of allowed devices:
/devices/allowedDevices.txt
#### Scanners:
/scanner/activeScan.py   
/scanner/passiveScan.py
#### Service script:
/systemd/deviceScanner.service
