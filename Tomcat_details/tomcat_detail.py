#!/usr/bin/env python
# coding:utf-8

import re
import json
import os
import sys
import psutil


# 主要信息获取function
def run(file):
  state = {}
  with open(file, "r+") as f:
    for v in f.readlines():
      if re.findall("SHUTDOWN", v):
        state["SHUTDOWN_PORT"] =  "%s" %(re.search("port=\"([0-9]+)\"", v).group(1))
      elif re.findall("org.apache.coyote.http11.Http11NioProtocol", v):
        if state.get("PORT01"):
          state["PORT02"] = "%s" %(re.search("port=\"([0-9]+)\"", v).group(1))
        else:
          state["PORT01"] = "%s" %(re.search("port=\"([0-9]+)\"", v).group(1))
      elif re.search(r"AJP\/1.3", v):
        state["JSP_PORT"] = "%s" %(re.search(r"port=\"([0-9]+)\"", v).group(1))

  state["Work_name"] = "%s" %(file.split("/")[-3])

  path = re.search("^(.*)/conf/server.xml", file).group(1)

  state["Path"] = path

  project = os.path.join(path, "webapps")

  if os.path.isdir(project):
    state["Project"] = os.listdir(project)
  f.close()
  return state

# 获取正在运行的Tomcat信息
result = {}
pids = psutil.pids()
for i in pids:
  if psutil.Process(i) == False:
    pass
  else:
    pid = psutil.Process(i)
    if pid.name() == "java" and re.search("tomcat", pid.cwd()):
      res = run(pid.cwd().replace("bin", "conf/server.xml"))
      result[res["Work_name"]] = res
	  
# 将信息写入文件	  
with open(r"%s.txt" %(os.uname()[1]), "w+") as f:
  f.write(str(result))

f.close()
