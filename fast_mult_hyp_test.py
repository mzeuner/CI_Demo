from hypothesis import given, example, settings, strategies as st
from fast_mult import mul_poly, karatsuba

@given(p=st.lists(st.integers()),q=st.lists(st.integers()))
@settings(max_examples=1000)
@example(p=[0],q=[])
def test_randomized(p,q):
    assert(mul_poly(p,q) == karatsuba(p,q))
