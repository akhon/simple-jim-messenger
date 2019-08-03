#!/usr/bin/env python3

from socket import *
from time import time, strftime, localtime
import pickle
import helpers


class Client:
    def __init__(self, addr, port, name):
        self.name = name
        self.addr = addr
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)


    def connect(self):
        try:
            self.socket.connect((self.addr, self.port))
            print("Successfully connected to {}:{}".format(self.addr, self.port))
        except Exception as e:
            print(e)

        # crafting presense message and sending to the server
        self.send(self.craft_presense())
        response = self.receive()
        self.parse(pickle.loads(response))


    def craft_presense(self):
        # TODO: move into Message class
        msg = {
            'action': 'presence',
            'time': time(),
            'type': 'status',
            'user': {
                'account_name': self.name,
                'status': 'Yep, I am here!'
            }
        }
        return pickle.dumps(msg)


    def send(self, msg):
        self.socket.send(bytes(msg))


    def receive(self):
        return self.socket.recv(helpers.MESSAGE_SIZE)


    def parse(self, msg):
        if msg['response'] == 200:
            print('Server response OK at {}'.format(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime(msg['time']))))
        else:
            print('Something went wrong')


    def close(self):
        self.socket.close()


    def whoami(self):
        return self.name


def main():
    console_args = helpers.args()
    c = Client(console_args.addr, console_args.port, 'Skywalker')
    c.connect()
    c.close()


if __name__ == '__main__':
    main()
