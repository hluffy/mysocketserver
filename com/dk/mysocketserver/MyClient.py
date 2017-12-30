import socket

client = socket.socket()
client.connect(('localhost',9999))

while True:
    data = input('>>: ').strip()
    if len(data)==0:
        continue
    client.send(data.encode('utf-8'))
    result = client.recv(1024)
    print(result.decode())
    pass