#!/usr/bin/env python
from random import random
from time import sleep

from base10 import MetricHelper, MetricHandler
from base10.dialects import JSONDialect
from base10.transports import RabbitMQWriter

if __name__ == '__main__':

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
        _writer = RabbitMQWriter(
            broker='127.0.0.1', exchange='amq.topic', topic='metrics.example')

    json = JSON()

    while True:
        json.write(MyMetric(value=random(), hostname='test'))
        sleep(1)
