import nmap
import time

nm = nmap.PortScanner()
o=open('/opt/deviceScanner/devices/Output.txt','a+')
nm.scan(hosts='192.168.24.0/24', arguments='-sP -n')
for h in nm.all_hosts():
	if 'mac' in nm[h]['addresses']:
		scanR = (nm[h]['addresses'])

		if (str(scanR)+'\n') not in open('/opt/deviceScanner/devices/allowedDevices.txt').read():
			o.write(str(scanR)+' Not in allowedDevices.txt\n')
		else:
			o.write(str(scanR)+'\n')
