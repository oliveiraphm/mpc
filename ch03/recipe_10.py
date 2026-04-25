def fact_r(n: int) -> int:
    if n == 0:
        return 1
    return n * fact_r(n-1)

from collections.abc import Iterable
def prod_i(int_iter: Iterable[int]) -> int:
    p = 1
    for x in int_iter:
        p *= x
    return p

from math import prod
def fact(n: int):
    return prod(range(1, n+1))

def ugly_fact(n: int) -> int:
    p = n
    while n != 1:
        n = n-1 
        p *= n
    return p

def fibo(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

from functools import cache

@cache
def fibo_r(n: int) -> int:
    if n < 2:
        return 1
    else:
        return fibo_r(n-1) + fibo_r(n-2)
    
from collections.abc import Iterator

def fibo_iter() -> Iterator[int]:
    a = 1
    b = 1
    yield a
    while True:
        yield b
        a, b = b, a + b

def fibo_i(n: int) -> int:
    for i, f_i in enumerate(fibo_iter()):
        if i == n:
            break
        return f_i
    
test_fact_r = """
>>> fact_r(5)
120
"""

test_prod_i_fact = """
>>> prod_i(range(1, 6))
120
>>> fact(5)
120
"""

test_ugly_fact = """
>>> ugly_fact(5)
120
>>> loop_fact(5)
120
"""

test_fibo_1 = """
>>> fibo(10)
89
>>> fibo_r(10)
89
"""

test_fibo_2 = """
>>> fibo_i(10)
89
"""

__test__ = {name: code for name, code in locals().items() if name.startswith("test_")}