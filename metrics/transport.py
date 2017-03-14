from .helpers import Transport


class FileTransport(Transport):
    def __init__(self, *args, **kwargs):
        self._n = 0

    def read(self):
        self._n += 1
        if self._n % 2:
            return """
            {
                "name": "cpu_usage",
                "fields": {
                    "user": 0.2,
                    "free": 0.75
                },
                "metadata": {
                    "hostname": "host-1"
                },
                "timestamp": 1489478831
            }
            """
        else:
            return """
            {
                "name": "memory_usage",
                "fields": {
                    "used": 0.2,
                    "free": 0.75
                },
                "metadata": {
                    "hostname": "host-1"
                },
                "timestamp": 1489478831
            }
            """

    def write(self, string):
        return True


class RabbitMQTransport(Transport):
    pass


class UDPTransport(Transport):
    pass
