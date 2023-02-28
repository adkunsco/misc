from fuel import convert, gauge
import pytest

def test_fuel():
    assert convert('3/4') == 75


def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

def test_letters():
    with pytest.raises(ValueError):
        convert('a/b')