import pytest
from myproj import A, B

def test_squared_sum():
    assert A.squared_sum(2, 3) == 25
    assert A.squared_sum(-2, 3) == 1
    assert A.squared_sum(2, -3) == 1
    assert A.squared_sum(-2, -3) == 25

def test_sum_squared():
    assert B.sum_squared(2, 3) == 13
    assert B.sum_squared(-2, 3) == 13
    assert B.sum_squared(2, -3) == 13
    assert B.sum_squared(-2, -3) == 13

