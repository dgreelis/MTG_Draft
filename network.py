import socket
import pickle
import struct
import sys

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.94.207.207"
        self.port = 5554
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def get_player_num(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send_pick(self, data):
        try:
            data = str(data)
            self.client.send(str.encode(data))
            # self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)

    def send_and_receive(self, data):
        try:
            data = str(data)
            self.client.send(str.encode(data))
            # self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)