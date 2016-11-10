#coding=gbk

import BaseHTTPServer
#import  http.server   # for py3

'''
第一个web服务器吧， 基本概念非常简单：

1.等待某个人连接我们的服务器并向我们发送一个HTTP请求
2.解析该请求
3.了解该请求希望请求的内容
4.服务器根据请求抓取需要的数据（从服务器本地文件中读或者程序动态生成）
5.将数据格式化为请求需要的格式
6.送回HTTP响应

步骤1，2，6的操作对所有web应用都是一样的，这部分内容Python标准库中的 BaseHTTPServer 模块可以帮助我们处理。我们只需要关注步骤3～5。

作者：Wayne Shi
链接：https://zhuanlan.zhihu.com/p/21323273
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''



class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):    #续写  ~Handler类  处理do_GET方法
	'''续写handler类'''
	#页面魔板
	page='''\
	<html>
	<body>
	<p>Hello, Web!</p>
	</body>
	</html>
	'''

	#具体处理一个GET请求的代码
	def do_GET(self):
		#格式化响应文本
		self.send_response(200)   #写响应代码
		self.send_header("Content-Type","text/html")   #编写响应头
		self.send_header("Content-Length",str(len(self.page)))
		self.end_headers()
		self.wfile.write(self.page)  #响应  内容

if __name__ == '__main__':
	serverAddress=("",82)
	server=BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
	server.serve_forever()
