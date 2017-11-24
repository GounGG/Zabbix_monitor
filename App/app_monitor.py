#!/usr/bin/env python
# coding:utf-8
from psutil import pids,Process
import re
import json
import sys

def F_Process(pname):
    result = []
    a = pids()
    for i in a:
	try:
            p = Process(i)
            if p.name() == 'java':
	        cmd = ' '.join(p.cmdline())
		if re.search(pname, cmd):
		    result.append(0)
		else:
		    result.append(1)
    	except Exception,e:
            continue
    if 0 in result and result.count(0) == 1:
        print 0
    else:
        print 1

def F_Memory(pname):
    a = pids()
    for i in a:
	try:
            p = Process(i)
            if p.name() == 'java':
                cmd = ' '.join(p.cmdline())
                if re.search(pname, cmd):
	            print round(p.memory_percent(), 2)
    	except Exception,e:
	    continue

def F_Threads(pname):
    a = pids()
    for i in a:
	try:
            p = Process(i)
            if p.name() == 'java':
            	cmd = ' '.join(p.cmdline())
            	if re.search(pname, cmd):
	            print p.num_threads()
    	except Exception,e:
	    continue

pname = sys.argv[1]
param = sys.argv[2]
 
if pname == 'Process':
    F_Process(param)
elif pname == 'Memory':
    F_Memory(param)
elif pname == "Threads":
    F_Threads(param)
