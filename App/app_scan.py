#!/usr/bin/env python
# coding:utf-8

import psutil
import re
import json

def thread():
    try:
	data = []
	name = []
        a = psutil.pids()
        for i in a:
            p = psutil.Process(i)
            if p.name() == 'java':
		if re.search('jar', p.cmdline()[-1]):
		     name.append(p.cmdline()[-1].split('-')[0])
 	for i in name:
	    data.append({'{#PNAME}': i})
	print json.dumps({'data': data}, indent=2)
    except Exception,e:
        print e

thread()
