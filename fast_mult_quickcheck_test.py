import pytest
from pytest import list_of
from fast_mult import mul_poly, karatsuba

@pytest.mark.randomize(p=list_of(int), q=list_of(int), ncalls=100)
def test_randomized(p,q):
    assert(mul_poly(p,q) == karatsuba(p,q))
