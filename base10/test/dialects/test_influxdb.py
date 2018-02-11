from time import time

import pytest

from base10.base import Dialect, Metric
from base10.dialects.influxdb_dialect import InfluxDBDialect


class TestInfluxDB:
    def test_construction(self):
        assert isinstance(InfluxDBDialect(), Dialect)

    def test_to_string(self):
        timestamp = time()

        metric_name = 'metric'
        metric_fields = ['value', 'string']
        metric_metadata = ['hostname']
        metric_values = {
            'value': 0,
            'string': 'test',
            'hostname': 'test',
            'time': timestamp
        }

        metric = Metric(
            metric_name, metric_fields, metric_metadata, **metric_values
        )

        dialect = InfluxDBDialect()
        string_repr = dialect.to_string(metric)

        assert string_repr == 'metric,hostname=test string="test",value=0 {}'.format(
            int(timestamp * 1e6)
        )
