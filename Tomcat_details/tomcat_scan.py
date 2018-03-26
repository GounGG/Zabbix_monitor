#!/usr/bin/env python
# coding:utf-8

import re
import json
import os
import sys
import psutil

# 定义一个类
class Scan():
  # 封装tomcat详细信息
  def run(self, file):
    state = {}
    with open(file, "r+") as f:
      for v in f.readlines():
        if re.findall("SHUTDOWN", v):
          state["{#SHUTDOWN_PORT}"] =  "%s" %(re.search("port=\"([0-9]+)\"", v).group(1))
        elif re.findall("org.apache.coyote.http11.Http11NioProtocol", v):
          if state.get("{#PORT01}"):
            state["{#PORT02}"] = "%s" %(re.search("port=\"([0-9]+)\"", v).group(1))
          else:
            state["{#PORT01}"] = "%s" %(re.search("port=\"([0-9]+)\"", v).group(1))
        elif re.search(r"AJP\/1.3", v):
          state["{#JSP_PORT}"] = "%s" %(re.search(r"port=\"([0-9]+)\"", v).group(1))
    state["{#Work_name}"] = "%s" %(file.split("/")[-3])
    path = re.search("^(.*)/conf/server.xml", file).group(1)
    state["{#Path}"] = path
    project = os.path.join(path, "webapps")
    if os.path.isdir(project):
      state["{#Project}"] = os.listdir(project)
    return state

  def result(self):
    result = []
    pids = psutil.pids()
    for i in pids:
      if psutil.Process(i) == False:
        pass
      else:
        pid = psutil.Process(i)
	try:
      # cwd()函数涉及到权限，目前采用sodu来解决权限问题，如果不想使用，可以截取cmdline()函数的返回信息
	  if pid.name() == "java" and re.search("tomcat", pid.cwd()):
            res = self.run(pid.cwd().replace("bin", "conf/server.xml"))
	    result.append(res)
	  else:
	    pass
	except Exception,e:
	  pass
          #result[res["Work_name"]] = res
    # 格式封装，满足zabbix需要的json格式
    return json.dumps({"data": result},indent=2)

print(Scan().result())