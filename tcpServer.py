import socket
import threading
import time
class TcpServer :
    def __init__(self , HOST = "192.168.1.31" , PORT=3000) :
        self.HOST = HOST 
        self.PORT = PORT 
    def start(self) :
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        ADDR = (self.HOST , self.PORT)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(ADDR)
        sock.listen()
        print("server listen at : " , sock.getsockname()) 
        while True :
            conn , addr = sock.accept()
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            response = self.request_handler(data)
            # print(response)
            conn.sendall(response)
            conn.close()

    # def setup(self , conn , addr) :
    #     while True :
    #         data = conn.recv(1024)
    #         response = self.request_handler(data)
    #         # print(response)
    #         conn.sendall(response)
    #         conn.close()
    #         time.sleep(1)