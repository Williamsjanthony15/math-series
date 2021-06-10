from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series

def test_version():
  assert __version__ == '0.1.0'

def test_fourTestFibo():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected

def test_eightTestFibo():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected

def test_fourTestLucas():
    actual = lucas(4)
    expected = 4
    assert actual == expected 

def test_eightTestLucas():
    actual = lucas(8)
    expected = 29
    assert actual == expected 

def test_fourSeriesSum():
    actual = sum_series(4)
    expected = 2
    assert actual == expected

def test_eightSeriesSum():
    actual = sum_series(8)
    expected = 13
    assert actual == expected
