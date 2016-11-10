#coding=gbk

import BaseHTTPServer
#import  http.server   # for py3


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
