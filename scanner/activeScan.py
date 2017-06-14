import nmap
import time
import yaml
import logging
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

my_logger.addHandler(handler)

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

while True:
	nm = nmap.PortScanner()
	o=open('/opt/deviceScanner/devices/Output.txt','a+')
	nm.scan(hosts = subnet, arguments = '-sP -n')
	for h in nm.all_hosts():
		if 'mac' in nm[h]['addresses']:
			scanR = (nm[h]['addresses'])
	
			if (str(scanR)+'\n') not in v:
				my_logger.info(str(scanR)+' Not in allowedDevices.txt')
				o.write(str(scanR)+'\n')
	time.sleep(interval)
