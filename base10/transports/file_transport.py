from base10.base import Reader, Writer
from base10.exceptions import TransportError


class FileReader(Reader):
    def __init__(self, filename, mode='r'):
        try:
            self._file = open(filename, mode)
        except IOError as e:
            raise TransportError('Could not open file "{}"'.format(filename),
                                 e)

    def read(self):
        for line in self._file:
            yield line


class FileWriter(Writer):
    def __init__(self, filename, mode='w'):
        try:
            self._file = open(filename, mode)
        except IOError as e:
            raise TransportError('Could not open file "{}"'.format(filename),
                                 e)

    def write(self, string):
        self._file.write(string + '\n')
        return True
