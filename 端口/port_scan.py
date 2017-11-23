#!/usr/bin/env python

import socket
import json

ports = {'http': 80, 
	 'https': 443, 
	 'ftp': 21, 
	 'activemq': 61616, 
	 'zookeeper': 2181, 
	 'restapi': 3333, 
	 'ssh': 2200,
	 'oracle': 1521,
	 'accounts-service': 2222,
	 'balance-service': 2232,
	 'bankservice': 1217,
	 'manage-service': 3335,
	 'order-service': 3322,
	 'paybaofoo-service': 7135,
	 'products-service': 4444,
	 'quote-service': 3353,
	 'schedule-service': 2242,
	 'sms-service': 1827,
	 'token-service': 3334,
	}

def Verify(port):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect(('localhost', port))
    s.close()
    return True
  except Exception,e:
    return False

data = []
for p in ports.keys():
    if Verify(ports[p]):
      data.append({'{#PNAME}': p, '{#PORT}': ports[p]})

print json.dumps({"data": data}, indent=2)
