from base10.base import Metric
from base10.utils import count_summarise


class TestUtils:

    def test_count_summarise_no_window(self):

        def gen():
            yield Metric(name='test', fields=['value'], metadata=[], value=1.0)
            yield Metric(name='test', fields=['value'], metadata=[], value=2.0)
            yield Metric(name='test', fields=['value'], metadata=[], value=3.0)
            yield Metric(name='test', fields=['value'], metadata=[], value=4.0)

        summary = count_summarise(gen())

        assert next(summary).values['value'] == 1.0
        assert next(summary).values['value'] == 2.0
        assert next(summary).values['value'] == 3.0
        assert next(summary).values['value'] == 4.0

    def test_count_summarise_window_1(self):

        def gen():
            yield Metric(name='test', fields=['value'], metadata=[], value=1.0)
            yield Metric(name='test', fields=['value'], metadata=[], value=2.0)
            yield Metric(name='test', fields=['value'], metadata=[], value=3.0)
            yield Metric(name='test', fields=['value'], metadata=[], value=4.0)

        summary = count_summarise(gen(), 2)

        assert next(summary).values['value'] == 1.5
        assert next(summary).values['value'] == 3.5

    def test_count_summarise_window_2(self):

        def gen():
            yield Metric(
                name='test', fields=['value1'], metadata=[], value1=1.0)
            yield Metric(
                name='test', fields=['value2'], metadata=[], value2=2.0)
            yield Metric(
                name='test', fields=['value1'], metadata=[], value1=3.0)
            yield Metric(
                name='test', fields=['value2'], metadata=[], value2=4.0)

        summary = count_summarise(gen(), 2)

        assert next(summary).values['value1'] == 2.0
        assert next(summary).values['value2'] == 3.0

    def test_count_summarise_string(self):

        def gen():
            yield Metric(name='test', fields=['value'], metadata=[], value='a')
            yield Metric(name='test', fields=['value'], metadata=[], value='b')
            yield Metric(name='test', fields=['value'], metadata=[], value='c')
            yield Metric(name='test', fields=['value'], metadata=[], value='d')

        summary = count_summarise(gen())

        assert next(summary).values['value'] == 'a'
        assert next(summary).values['value'] == 'b'
        assert next(summary).values['value'] == 'c'
        assert next(summary).values['value'] == 'd'
