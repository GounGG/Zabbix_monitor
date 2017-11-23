#!/usr/bin/env python

import socket
import json

ports = {'http': 80, 
	 'https': 443, 
	 'ftp': 21, 
	 'activemq': 61616, 
	 'zookeeper': 2181, 
	 'ssh': 2200,
	 'oracle': 1521,
	}

# 使用socket模块，查看端口是否可以连接。
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
