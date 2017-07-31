#!/usr/bin/env python
from random import random
from time import sleep

from base10 import MetricHelper, MetricHandler
from base10.dialects import InfluxDBDialect
from base10.transports import UDPWriter

if __name__ == '__main__':

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
