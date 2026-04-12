test_example_1 = """
>>> import math

>>> help(math.sin)
Help on built-in function sin in module math:
<BLANKLINE>
sin(x, /)
    Return the sine of x (measured in radians).
<BLANKLINE>


>>> import math
>>> math.sin(x=0.5)
Traceback (most recent call last):
...
TypeError: math.sin() takes no keyword arguments
"""

def F_1(c: float) -> float:
    return 32 + 9 * c / 5

def F_2(c: float, /) -> float:
    return 32 + 9 * c / 5

def C(f: float, /, truncate: bool=False) -> float:
    c = 5 * (f - 32) / 9
    if truncate:
        return round(c, 0)
    return c

test_example_2 = """
>>> C(72)
22.22222222222222

>>> C(72, truncate=True)
22.0

>>> C(72, True)
22.0
"""

test_example_1 = """
>>> F_1(-25)
-13.0
>>> F_2(-25)
-13.0
"""

__test__ = {name: code for name, code in locals().items() if name.startswith("test_")}