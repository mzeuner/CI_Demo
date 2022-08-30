"""

This file contains some basic functions for computing with polynomials.
Polynomials are encoded as lists of coefficients increasing in degree.
So the polynomial 3x^2 + 2x + 1 corresponds to the list [1,2,3] etc...

In particular we give two ways of multiplying polynomials.
The naive/standard way is in O(n) and the faster way using Karatsuba's method
is in O(n ^ log(3)).

It is however not easy to see that these two algorithms always
produce the same result, so we want to do some testing!

"""


## preliminaries
def add_poly(p,q):
    res = [];
    if p==[]:
        return q
    elif q==[]:
        return p
    elif len(p) <= len(q):
        for i in range(0,len(q)):
            if i < len(p):
                res.append(p[i]+q[i])
            else:
                res.append(q[i])
    else:
        for i in range(0,len(p)):
            if i < len(q):
                res.append(p[i]+q[i])
            else:
                res.append(p[i])
    return res



def neg_poly(p):
    return list(map(lambda x: -x,p))


def sub_poly(p,q):
    return add_poly(p,neg_poly(q))


## help functions from functional programming
def my_repeat(i,x):
    res = []
    for j in range(0,i):
        res.append(x)
    return res

def my_take(n,p):
    res=[]
    for i in range(0,n):
        res.append(p[i])
    return res

def my_drop(n,p):
    res=[]
    for i in range(n,len(p)):
        res.append(p[i])
    return res


## a function adding n zeroes at the beginning of,
## corresponds to multiplying p with x^n
def shift_right(n,p):
    res = my_repeat(n,0)
    res.extend(p)
    return res

### the naive way to multiply polynomials
def mul_poly(p,q):
    res=[]
    if p==[] or q==[]:
        return []
    else:
        for i in range(0,len(p)):
            snd = shift_right(i,list(map(lambda x: x*p[i],q)))
            res = add_poly(res,snd)
    return res

## Karatsuba's algorithm for fast multiplication
def karatsuba(p,q):
    if len(p)<=2 or len(q)<=2:
        return mul_poly(p,q)
    else:
        m = min(len(p) // 2, len(q) // 2)
        a = my_drop(m,p)
        b = my_take(m,p)
        c = my_drop(m,q)
        d = my_take(m,q)
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        a_plus_b = add_poly(a,b)
        c_plus_d = add_poly(c,d)
        ad_plus_bc = sub_poly(sub_poly(karatsuba(a_plus_b, c_plus_d), ac), bd)

        return add_poly(shift_right(2*m,ac), add_poly(shift_right(m,ad_plus_bc), bd))



def main():
    print(mul_poly([1,2],[3,4]))
    print(karatsuba([1,2,3,4,5],[6,7,8,9,10]))
    print(mul_poly([1,2,3,4,5],[6,7,8,9,10]))


if __name__ == "__main__":
    main()
