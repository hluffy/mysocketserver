# socketserver		
import socketserver		
1.创建一个类，该类继承socketserver.BaseRequestHandler,并重写handle方法		
2.实例化socketserver		
`server = socketserver.ThreadingTCPServer(host,handle类)`		
`server.serve_forever()`		
socketserver.ThreadingTCPServer()方法支持多线程		
socket.server_forever()一直监听