import pytest
from base10.base import Dialect
from base10.exceptions import DialectError


class TestDialects:

    def test_dialect_construction(self):
        assert isinstance(Dialect(), Dialect)

    def test_dialect_from_string_exception(self):
        dialect = Dialect()

        with pytest.raises(DialectError) as exc:
            dialect.from_string('')

        assert 'Attempt to read with a write-only dialect' == str(exc.value)

    def test_dialect_to_string_exception(self):
        dialect = Dialect()

        with pytest.raises(DialectError) as exc:
            dialect.to_string(None)

        assert 'Attempt to write with a read-only dialect' == str(exc.value)
