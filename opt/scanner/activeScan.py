import nmap
nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.0/28', arguments='-sP -n')
for h in nm.all_hosts():
	if 'mac' in nm[h]['addresses']:
		scanR = (nm[h]['addresses'])

		if (str(scanR)+'\n') not in open('/opt/devices/allowedDevices.txt').read():
			open('/opt/devices/Output.txt').write('True')
			print ("true")
		else:
			open('/opt/devices/Output.txt').write('False')
			print ("false")
