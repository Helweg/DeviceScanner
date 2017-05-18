import nmap
nm = nmap.PortScanner()
o=open('/opt/scanner/opt/devices/Output.txt','w+')
nm.scan(hosts='192.168.80.0/24', arguments='-sP -n')
for h in nm.all_hosts():
	if 'mac' in nm[h]['addresses']:
		scanR = (nm[h]['addresses'])

		if (str(scanR)+'\n') not in open('/opt/scanner/opt/devices/allowedDevices.txt').read():
			o.write(str(scanR)+'\n')
			print ("true")
		else:
			o.write(str(scanR)+'\n')
			print ("false")
