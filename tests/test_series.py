from math_series import __version__
from math_series.series import fibonacci, lucas

def test_version():
  assert __version__ == '0.1.0'

def fourTestFibo():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected

def eightTestFibo():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected

def fourTestLucas():
    actual = lucas(4)
    expected = 4
    assert actual == expected 

def eightTestLucas():
    actual = lucas(8)
    expected = 29
    assert actual == expected 

def fourSeriesSum():
    actual = fourSeriesSum(4)
    expected = 2
    assert actual == expected

def eightSeriesSum():
    actual = eightSeriesSum(8)
    expected = 4
    assert actual == expected
