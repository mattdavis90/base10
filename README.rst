Base10
======
Base10 is a metrics abstraction layer.

|Version| |Status| |Coverage| |License| |Docs|

Introduction
------------
Base10 is a metrics abstractoin layer for linking multiple metrics source and stores. It also simplifies metric creation and proxying.

Documentation
-------------
Base10's documentation can be found at `https://base10.readthedocs.io <https://base10.readthedocs.io>`

Example
-------
This shows a simple metric generator that writes a JSON formatted metric, containing a random value, to RabbitMQ.

.. code :: python
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
        _writer = RabbitMQWriter(broker='127.0.0.1',
                                 exchange='amq.topic',
                                 topic='metrics.example')
    
    json = JSON()
    
    while True:
        json.write(MyMetric(value=random(), hostname='test'))
        sleep(1)

This shows a simple proxy that reads JSON formatted metrics from RabbitMQ and outputs them in InfluxDB format over a UDP socket.

.. code :: python
    from base10 import MetricHandler
    from base10.dialects import JSONDialect, InfluxDBDialect
    from base10.transports import RabbitMQReader, UDPWriter
    
    class RabbitMQ(MetricHandler):
        _dialect = JSONDialect()
        _reader = RabbitMQReader(broker='127.0.0.1',
                                 exchange='amq.topic',
                                 routing_key='metrics.#')
    
    class InfluxDB(MetricHandler):
        _dialect = InfluxDBDialect()
        _writer = UDPWriter(host='127.0.0.1', port=10000)
    
    rabbitmq = RabbitMQ()
    influxdb = InfluxDB()
    
    for metric in rabbitmq.read():
        influxdb.write(metric)

Contributing
------------
To contribute to pika, please make sure that any new features or changes
to existing functionality **include test coverage**.

*Pull requests that add or change code without coverage will most likely be rejected.*

Additionally, please format your code using `yapf <http://pypi.python.org/pypi/yapf>`_
with ``google`` style prior to issuing your pull request (:bash:`yapf --style=google -i -r base10`).

.. |Version| image:: https://img.shields.io/pypi/v/base10.svg?
   :target: http://badge.fury.io/py/base10

.. |Status| image:: https://img.shields.io/travis/mattdavis90/base10.svg?
   :target: https://travis-ci.org/mattdavis90/base10

.. |Coverage| image:: https://img.shields.io/codecov/c/github/mattdavis90/base10.svg?
   :target: https://codecov.io/github/mattdavis90/base10?branch=master

.. |License| image:: https://img.shields.io/pypi/l/base10.svg?
   :target: https://base10.readthedocs.io

.. |Docs| image:: https://readthedocs.org/projects/base10/badge/?version=stable
   :target: https://base10.readthedocs.io
   :alt: Documentation Status
