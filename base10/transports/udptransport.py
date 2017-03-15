from socket import socket, AF_INET, SOCK_DGRAM

from base10.base import Transport
from base10.exceptions import TransportError


class UDPTransport(Transport):
    def __init__(self, host, port):
        self._host = host
        self._port = port

        self._socket = socket(AF_INET, SOCK_DGRAM)

    def read(self):
        raise TransportError('Can\'t read from UDPTransport yet',
                             NotImplementedError())

    def write(self, string):
        self._socket.sendto(string + '\n', (self._host, self._port))
