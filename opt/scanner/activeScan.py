import nmap
nm = nmap.PortScanner()
o=open('/opt/devices/Output.txt','w+')
nm.scan(hosts='192.168.1.0/24', arguments='-sP -n')
for h in nm.all_hosts():
	o.write(h+'\n')
	if 'mac' in nm[h]['addresses']:
		scanR = (nm[h]['addresses'])

		if (str(scanR)+'\n') not in open('/opt/devices/allowedDevices.txt').read():
			o.write(str(scanR)+'\n')
			print ("true")
		else:
			o.write(str(scanR)+'\n')
			print ("false")
