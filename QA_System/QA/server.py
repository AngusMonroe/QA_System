import socket

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    print("create socket succ!")

    sock.bind(('10.17.152.6',8080))
    print('bind socket succ!')

    sock.listen(5)
    print('listen succ!')

except:
    print("init socket error!")

while True:
    print("listen for client...")
    conn,addr=sock.accept()
    print("get client")
    print(addr)

    conn.settimeout(30)
    szBuf=conn.recv(1024)
    print("recv:"+str(szBuf,'utf-8'))

    if "0"==szBuf:
        conn.send(b"exit")
    else:
        conn.send(szBuf)

    conn.close()
    print("end of servive")