from .helpers import Transport


class FileTransport(Transport):
    def __init__(self, filename, mode='r+'):
        try:
            self._file = open(filename, mode)
        except IOError:
            raise IOError('Could not open file "{}"'.format(filename))

    def read(self):
        for line in self._file:
            yield line

    def write(self, string):
        self._file.write(string + '\n')
        return True


class RabbitMQTransport(Transport):
    pass


class UDPTransport(Transport):
    pass
