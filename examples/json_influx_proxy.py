#!/usr/bin/env python
from base10 import MetricHandler
from base10.dialects import JSONDialect, SplunkDialect  #InfluxDBDialect
from base10.transports import RabbitMQReader, UDPWriter

if __name__ == '__main__':

    class RabbitMQ(MetricHandler):
        _dialect = JSONDialect()
        _reader = RabbitMQReader(
            broker='127.0.0.1', exchange='amq.topic', routing_key='metrics.#')

    class InfluxDB(MetricHandler):
        _dialect = SplunkDialect()  #InfluxDBDialect()
        _writer = UDPWriter(host='127.0.0.1', port=10000)

    rabbitmq = RabbitMQ()
    influxdb = InfluxDB()

    for metric in rabbitmq.read():
        influxdb.write(metric)
