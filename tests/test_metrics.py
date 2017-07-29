from base10 import MetricHelper
from base10.base import Metric


class TestMetrics:

    def test_somethign(self):

        class MyMetric(MetricHelper):
            _name = 'metric'

            _fields = [
                'value',
            ]

            _metadata = [
                'hostname',
            ]

        metric = MyMetric(value=0, hostname='test')

        assert (isinstance(metric, Metric))
