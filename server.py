# import SocketServer
import socket
import sys
import time

class Server:

    ADDRESS = 0
    PORT = 0
    sock_obj = 0
    conn = 0

    def __init__(self, ADDRESS, PORT):
        self.ADDRESS = ADDRESS
        self.PORT = PORT
        try: 
            self.sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock_obj.bind((self.ADDRESS, self.PORT))
            print("socket is initialized")
            self.listen()
        except socket.error as sock_err: 
            print("Socket could instantiate socket: %s" %sock_err)
        finally: 
            sys.exit()

        


    def listen(self):
        self.sock_obj.listen(5)
        print("Server is listening")

        self.conn, addr = self.sock_obj.accept()
        print("Got connection from:", addr)
        while True:
            data = self.conn.recv(1024).decode()
            if data:
                print("He said:", data)
                if data == "exit\n":
                    print("TRUE")
                    break
        self.conn.send("Tank u for Connecting \n")
        self.conn.close()

