import socket
import os
import json

class FtpClient(object):
    def __init__(self):
        pass

    def connect(self,ip,port):
        self.client = socket.socket()
        self.client.connect((ip,port))
        pass

    def help(self):
        msg = '''
            ls
            cd ../..
            put filename
            get filename
        '''

        print(msg)

    def interactive(self):
        while True:
            cmd = input('>>:').strip()
            if len(cmd) == 0:
                continue

            cmd_str = cmd.split()[0]
            if hasattr(self,'cmd_%s' % cmd_str):
                func = getattr(self,'cmd_%s' % cmd_str)
                func(cmd)
            else:
                self.help()
            pass
        pass

    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    'action':'put',
                    'filename':filename,
                    'size':filesize,
                    'overridden':True
                }
                self.client.send(json.dumps(msg_dic).encode('utf-8'))
                server_response = self.client.recv(1024)
                f = open(filename, 'rb')
                for line in f:
                    self.client.send(line)
                else:
                    f.close()

            else:
                print('file is not exist')
        pass

if __name__ == '__main__':
    ftp = FtpClient()
    ftp.connect('localhost',9999)
    ftp.interactive()