from numbers import Number
from time import time
from collections import defaultdict
from .base import Metric


class _Accumulator(object):

    def __init__(self):
        self._value = 0
        self._count = 0

    @property
    def value(self):
        if isinstance(self._value, Number):
            if self._count != 0:
                return self._value / self._count
            else:
                return 0
        else:
            return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, Number) and isinstance(self._value, Number):
            self._value += value
            self._count += 1
        else:
            self._value = value
            count = 1

    @property
    def count(self):
        return self._count


def count_summarise(metrics, window=1):
    accumulator_dict = defaultdict(lambda: defaultdict(_Accumulator))

    for metric in metrics:
        if metric is not None:
            name = metric.name
            metadata = tuple((k, v) for k, v in metric.values.iteritems()
                             if k in metric.metadata)

            for field, value in metric.values.iteritems():
                if field in metric.fields:
                    accumulator_dict[(name, metadata)][field].value = value

        for (name, metadata), accumulators in accumulator_dict.iteritems():
            fields = [
                key for key, accumulator in accumulators.iteritems()
                if accumulator.count >= window
            ]

            if len(fields) == 0:
                continue

            metadata = [key for (key, _) in metadata]

            values = {field: accumulators[field].value for field in fields}
            values.update({key: value for (key, value) in metadata})

            yield Metric(name=name, fields=fields, metadata=metadata, **values)

            for field in fields:
                del accumulators[field]
