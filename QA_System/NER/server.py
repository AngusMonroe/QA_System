import socket
import main

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("create socket succ!")

    sock.bind(('10.18.28.35', 8080))
    print('bind socket succ!')

    sock.listen(5)
    print('listen succ!')

except:
    print("init socket error!")

while True:
    print("listen for client...")
    conn, addr=sock.accept()
    print("get client")
    print(addr)

    conn.settimeout(30)
    szBuf = conn.recv(1024)

    print("recv:"+str(szBuf, 'utf-8'))
    m = main
    res = m.main(str(szBuf, 'utf-8'))
    # res[0] = "<a href=\"" + res[0] + "\">查看详情</a>"
    # res = ['There is a problem with the server.', 'Please contact the administrator to open the service.']
    szBuf = bytes(res[1] + '\n' + res[0], 'utf-8')

    if "0" == szBuf:
        conn.send(b"exit")
    else:
        conn.send(szBuf)

    conn.close()
    print("end of server")
