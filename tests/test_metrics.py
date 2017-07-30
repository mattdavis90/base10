from time import time
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

        assert (isinstance(metric, Metric))

    def test_metric_properties(self):
        now = time()
    
        metric = self.MyMetric(value=0, hostname='test', time=now)

        assert metric.name == 'metric'
        assert metric.fields == ['value']
        assert metric.metadata == ['hostname']
        assert metric.values == {'value': 0, 'hostname': 'test', 'time': now}
