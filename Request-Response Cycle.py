#Request-Response Cycle


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #\n new lines
mysock.send(cmd)

while True:
    data = mysock.recv(512) #get 512 chars each time
    if len(data) < 1: #if = 0 meaning the end of the string
        break
    print(data.decode(),end='')

mysock.close()
