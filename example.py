#!/usr/bin/env python


def json_sender():
    from random import random
    from time import sleep

    from base10 import MetricHelper, MetricHandler
    from base10.dialects import JSONDialect
    from base10.transports import RabbitMQWriter

    class MyMetric(MetricHelper):
        _name = 'metric'

        _fields = [
                'value',
                ]

        _metadata = [
                'hostname',
                ]

    class JSON(MetricHandler):
        _dialect = JSONDialect()
        _writer = RabbitMQWriter(host='127.0.0.1', port=10000)

    json = JSON()

    while True:
        json.write(MyMetric(value=random(), hostname='test'))
        sleep(1)


def json_to_influx_proxy():
    from base10 import MetricHandler
    from base10.dialects import JSONDialect, InfluxDBDialect
    from base10.transports import RabbitMQReader, UDPWriter

    class RabbitMQ(MetricHandler):
        _dialect = JSONDialect()
        _reader = RabbitMQReader(broker='127.0.0.1',
                                 exchange='exchange',
                                 binding='metrics.#')

    class InfluxDB(MetricHandler):
        _dialect = InfluxDBDialect()
        _writer = UDPWriter(host='127.0.0.1', port=10000)

    rabbitmq = RabbitMQ()
    influxdb = InfluxDB()

    for metric in rabbitmq.read():
        influxdb.write(metric)


def influx_sender():
    from random import random
    from time import sleep

    from base10 import MetricHelper, MetricHandler
    from base10.dialects import InfluxDBDialect
    from base10.transports import UDPWriter

    class MyMetric(MetricHelper):
        _name = 'metric'

        _fields = [
                'value',
                ]

        _metadata = [
                'hostname',
                ]

    class InfluxDB(MetricHandler):
        _dialect = InfluxDBDialect()
        _writer = UDPWriter(host='127.0.0.1', port=10000)

    influxdb = InfluxDB()

    while True:
        influxdb.write(MyMetric(value=random(), hostname='test'))
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
