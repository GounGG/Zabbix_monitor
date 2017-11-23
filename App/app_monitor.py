#!/usr/bin/env python

import psutil
import re
import json
import sys

def Process(name):
    result = []
    try:
        a = psutil.pids()
        for i in a:
            p = psutil.Process(i)
            if p.name() == 'java':
	        cmd = ' '.join(p.cmdline())
		if re.search(name, cmd):
		    result.append(0)
		else:
		    result.append(1)
    except Exception,e:
        print 1
    else:
	if 0 in result and result.count(0) == 1:
	    print 0
	else:
	    print 1

def Memory(name):
    a = psutil.pids()
    for i in a:
        p = psutil.Process(i)
        if p.name() == 'java':
            cmd = ' '.join(p.cmdline())
            if re.search(name, cmd):
	        print round(p.memory_percent(), 2)

name = sys.argv[1]
param = sys.argv[2] 
if name == 'Process':
    Process(param)
elif name == 'Memory':
    Memory(param)
