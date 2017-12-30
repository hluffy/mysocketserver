import socketserver

class MyTcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:


            # try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote.'.format(self.client_address))
                print(self.data.decode())
                if not self.data:
                    print('客户端断开连接')
                    break
                self.request.send(self.data.upper())
                # self.request.sendall(self.data.upper())
                pass


            # except ConnectionResetError as e:
            #     print('err ',e)
            #     break



if __name__ == '__main__':
    host = ('localhost',9999)
    # server = socketserver.TCPServer(host,MyTcpServer)
    # 多并发
    server = socketserver.ThreadingTCPServer(host,MyTcpServer)
    server.serve_forever()

    pass