# Tomcat_details	

步骤一：

**tomcat_detail.py**

​	在client主机上执行此脚本，可以生成本地运行tomcat的详细信息，包括端口等信息。

```json
{
	'tomcat_webapi': {
		'PORT02': '14843',
		'PORT01': '14808',
		'Work_name': 'tomcat_webapi',
		'Project': ['webapi', 'webapi.zip', 'webapi2017-07-31.zip', 'webapi2017-08-01.zip'],
		'SHUTDOWN_PORT': '14005',
		'Path': '/data/trade/www/tomcat_webapi',
		'JSP_PORT': '14009'
	}
}
```



步骤二：

**task.py**

​	此脚本是读取步骤一生成的文件，并生成execl文档。

