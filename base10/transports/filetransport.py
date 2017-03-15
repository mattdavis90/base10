from base10.base import Transport
from base10.exceptions import TransportError


class FileTransport(Transport):
    def __init__(self, filename, mode='r+'):
        try:
            self._file = open(filename, mode)
        except IOError as e:
            raise TransportError('Could not open file "{}"'.format(filename),
                                 e)

    def read(self):
        for line in self._file:
            yield line

    def write(self, string):
        self._file.write(string + '\n')
        return True
