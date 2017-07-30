import pytest
from base10.base import Reader, Writer


class TestTransports:

    def test_reader_construction(self):
        with pytest.raises(TypeError) as exc:
            reader = Reader()

        assert "Can't instantiate" in str(exc.value)

    def test_writer_construction(self):
        with pytest.raises(TypeError) as exc:
            writer = Writer()

        assert "Can't instantiate" in str(exc.value)
