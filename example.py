#!/usr/bin/env python


def fileproxy():
    from time import sleep
    from base10 import MetricHandler
    from base10.dialect import JSONDialect
    from base10.transport import FileTransport

    class FileIn(MetricHandler):
        _dialect = JSONDialect()
        _transport = FileTransport(filename='in', mode='r')

    class FileOut(MetricHandler):
        _dialect = JSONDialect()
        _transport = FileTransport(filename='out', mode='w')

    filein = FileIn()
    fileout = FileOut()

    for metric in filein.read():
        fileout.write(metric)
        sleep(1)


def filesender():
    from random import random
    from time import sleep
    from base10 import MetricHelper, MetricHandler
    from base10.dialect import JSONDialect
    from base10.transport import FileTransport

    class MyMetric(MetricHelper):
        _name = 'metric'

        _fields = [
                'value',
                ]

        _metadata = [
                'hostname',
                ]

    class FileOut(MetricHandler):
        _dialect = JSONDialect()
        _transport = FileTransport(filename='out', mode='w')

    fileout = FileOut()

    while True:
        fileout.write(MyMetric(value=random(), hostname='test'))
        sleep(1)


def proxy():
    from base10 import MetricHandler
    from base10.dialect import JSONDialect, InfluxDBDialect
    from base10.transport import RabbitMQTransport, UDPTransport

    class RabbitMQ(MetricHandler):
        _dialect = JSONDialect()
        _transport = RabbitMQTransport(broker='127.0.0.1',
                                       exchange='exchange',
                                       binding='metrics.#')

    class InfluxDB(MetricHandler):
        _dialect = InfluxDBDialect()
        _transport = UDPTransport(host='127.0.0.1', port=10000)

    rabbitmq = RabbitMQ()
    influxdb = InfluxDB()

    for metric in rabbitmq.read():
        influxdb.write(metric)


def sender():
    from random import random
    from time import sleep

    from base10 import MetricHelper, MetricHandler
    from base10.dialect import SplunkDialect
    from base10.transport import UDPTransport

    class MyMetric(MetricHelper):
        _name = 'metric'

        _fields = [
                'value',
                ]

        _metadata = [
                'hostname',
                ]

    class Splunk(MetricHandler):
        _dialect = SplunkDialect()
        _transport = UDPTransport(host='127.0.0.1', port=10000)
        _autocommit = True
        _bulk_size = 5

    splunk = Splunk()

    while True:
        splunk.write(MyMetric(value=random(), hostname='test'))
        sleep(1)


if __name__ == '__main__':
    from sys import argv, modules

    if len(argv) <= 1:
        print('Need an example to run. e.g.')
        print('\t{} proxy'.format(argv[0]))
        exit()

    this_module = modules[__name__]
    to_run = argv[1]

    if hasattr(this_module, to_run):
        getattr(this_module, to_run)()
    else:
        print('ERROR: Example "{}" not found'.format(to_run))
