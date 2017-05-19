import nmap
import time
import yaml

stream = open("scannerConf.yml", 'r')
docs = yaml.load_all(stream)
for doc in docs:
	for k,v in doc.items():
		if k == 'Allowed Devices':
			allowedDevices = v
		if k == 'Subnet':
			subnet = v
		if k == 'Interval':
			interval = v

file = open('/opt/deviceScanner/devices/allowedDevices.txt', 'a+')
for devices in allowedDevices:
	file.write(str(devices)+'\n')

nm = nmap.PortScanner()
o=open('/opt/deviceScanner/devices/Output.txt','a+')
nm.scan(hosts = subnet, arguments = '-sP -n')
for h in nm.all_hosts():
	if 'mac' in nm[h]['addresses']:
		scanR = (nm[h]['addresses'])

		if (str(scanR)+'\n') not in file:
			o.write(str(scanR)+' Not in allowedDevices.txt\n')
		else:
			o.write(str(scanR)+'\n')
