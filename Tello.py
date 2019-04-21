import socket
import threading

class Tello:
    def __init__(self):
        self.tello_adress = ('192.168.10.1', 8889)
        self.local_adress = ('', 9000)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_mess = ''
        self.error_flag = False

    
    def __receive(self):
        while True:
            try:
                self.recv_mess, server = self.sock.recvfrom(1518)
            except:
                self.error_flag = True
        
