import unittest
# from pytest import list_of
from karatsuba import mul_poly, karatsuba

class MyTestCase(unittest.TestCase):
    def test_mul_poly(self):
        p=[1,2]
        q=[3,4]
        r=[3,10,8]
        self.assertEqual(mul_poly(p,q),r)


    def test_manual(self):
        p=[1,2,3,4,5]
        q=[6,7,8,9,10]
        self.assertEqual(mul_poly(p,q), karatsuba(p,q))


    # @pytest.mark.randomize(p=list_of(int), q=list_of(int))
    # def test_randomized(self):
    #     self.assertEqual(mul_poly(p,q), karatsuba(p,q))



if __name__ == '__main__':
    unittest.main()
