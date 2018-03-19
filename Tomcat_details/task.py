# coding:utf-8

import os
import json
from xlwt import *
import re

w= Workbook(encoding='utf-8')
ws= w.add_sheet('001')
fnt = Font()
style = XFStyle()
style.font = fnt

# 读取Tomcat_detail执行生成的txt文档
path = u'C:/Users/Administrator/Desktop/details/test'

# 读写文件，生成execl报表
n = 0
for  f in os.listdir(path):
    ws.write(n + 1 , 0, re.search("^(.*)\.txt", f).group(1), style)
    file_path = os.path.join(path, f)
    with open(file_path.replace('\\', '/'), "r") as v:
        for x,y in (eval(v.readlines()[0])).items():
            ws.write(n + 1, 1, x, style)
            l = 1
            for z in y.values():
                ws.write(n + 1, l + 1, str(z), style)
                l = l + 1
            n += 1
                #ws.write(n + 1, x + 1, 1, style)

# 保存
w.save(u"test.xls")

