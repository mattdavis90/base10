from datetime import datetime
from abc import ABCMeta, abstractmethod


class Metric(object):
    def __init__(self, name, fields, metadata, **kwargs):
        self._name = name
        self._fields = fields
        self._metadata = metadata

        if 'time' in self._fields:
            self._fields.remove('time')

        self._verify_and_store(kwargs)

    def _verify_and_store(self, values):
        timestamp = values.pop('time', self._current_timestamp())

        if sorted(self._fields + self._metadata) != sorted(values.keys()):
            raise NameError('Expected {} but got {}'.format(
                sorted(self._fields + self._metadata),
                sorted(values.keys())
                ))

        self._values = values
        self._values['time'] = timestamp

    def _current_timestamp(self):
        return datetime.utcnow()

    @property
    def name(self):
        return self._name

    @property
    def fields(self):
        return self._fields

    @property
    def metadata(self):
        return self._metadata

    @property
    def values(self):
        return self._values

    def __repr__(self):
        return '<Metric:"{}" Fields:{} Metadata:{} Values:{}>'.format(
                self.name,
                self.fields,
                self.metadata,
                self.values)


class MetricHelper(Metric):
    __initialised__ = False

    def __new__(cls, *args, **kwargs):
        if not cls.__initialised__:
            if 'name' in kwargs:
                cls._name = kwargs.pop('name')
            else:
                if not hasattr(cls, '_name'):
                    raise ValueError('_name is required')

            if 'fields' in kwargs:
                cls._fields = kwargs.pop('fields')
            else:
                if not hasattr(cls, '_fields'):
                    raise ValueError('_fields is required')

            if 'metadata' in kwargs:
                cls._metadata = kwargs.pop('metadata')
            else:
                if not hasattr(cls, '_metadata'):
                    raise ValueError('_metadata is required')

            if 'time' in cls._fields:
                cls._fields.remove('time')

            cls.__initialised__ = True

        return super(Metric, cls).__new__(cls, *args, **kwargs)

    def __init__(self, **kwargs):
        self._verify_and_store(kwargs)


class MetricHandler(object):
    def __init__(self, *args, **kwargs):
        pass

    def read(self):
        while True:
            yield self._dialect.from_string(self._transport.read())

    def write(self, metric):
        return self._transport.write(self._dialect.to_string(metric))


class Dialect(object):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def from_string(self, string):
        pass

    @abstractmethod
    def to_string(self, metric):
        pass


class DialectError(Exception):
    pass


class Transport(object):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, string):
        pass
