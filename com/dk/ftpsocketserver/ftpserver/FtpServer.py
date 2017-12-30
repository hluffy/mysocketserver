import socketserver
import json

class TcpServer(socketserver.BaseRequestHandler):
    def put(self,*args):
        """接收客户端文件"""
        cmd_data = args[0]
        filename = cmd_data['filename']
        filesize = cmd_data['size']

        # 保存文件
        print(cmd_data)
        print('save file')
        print(filename)
        print(filesize)
        f = open(filename, 'wb')
        self.request.send(b'200 ok')

        received_size = 0
        while True:
            if received_size < filesize:
                data = self.request.recv(1024)
                f.write(data)
                received_size += len(data)
            else:
                print('file [%s] has uploaded...' % filename)

                f.close()
                break

        pass

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print('{} wrote.'.format(self.client_address))
            print(self.data)
            if not self.data:
                break

            cmd_dic = json.loads(self.data.decode())
            action = cmd_dic['action']
            if hasattr(self,action):
                func = getattr(self,action)
                func(cmd_dic)
        pass


if __name__ == '__main__':
    host = ('localhost',9999)
    server = socketserver.ThreadingTCPServer(host,TcpServer)
    server.serve_forever()