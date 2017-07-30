from time import time

import pytest
from base10 import MetricHelper
from base10.base import Metric


class TestMetrics:

    def setup_method(self):

        class MyMetric(MetricHelper):
            _name = 'metric'

            _fields = [
                'value',
            ]

            _metadata = [
                'hostname',
            ]

        self.MyMetric = MyMetric

    def test_metric_helper(self):
        metric = self.MyMetric(value=0, hostname='test')

        assert isinstance(metric, Metric)

    def test_metric_properties(self):
        metric_name = 'metric'
        metric_fields = ['value']
        metric_metadata = ['hostname']
        metric_values = {'value': 0, 'hostname': 'test', 'time': time()}

        metric = Metric(metric_name, metric_fields + ['time'], metric_metadata, **metric_values)

        assert metric.name == metric_name
        assert metric.fields == metric_fields
        assert metric.metadata == metric_metadata
        assert metric.values == metric_values

        assert repr(
            metric) == '<Metric:"{}" Fields:{} Metadata:{} Values:{}>'.format(
                metric_name, metric_fields, metric_metadata, metric_values)

    def test_metric_helper_exception(self):
        with pytest.raises(NameError) as exc:
            metric = self.MyMetric(value=0, host='test')

        assert "Expected ['hostname', 'value'] but got ['host', 'value']" in str(
            exc.value)
