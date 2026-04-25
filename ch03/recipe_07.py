def temperature(*, f_temp=None, c_temp=None):
    if c_temp is None:
        return {'f_temp': f_temp, 'c_temp':5*(f_temp-32)/9}
    elif f_temp is None:
        return {'f_temp': 32+9*c_temp/5, 'c_temp': c_temp}
    else:
        raise TypeError("One of f_temp or c_temp must be provided")
    
def temperature_1(*,
    f_temp: float | None = None,
    c_temp: float | None = None):
    ...

def temperature_2(*,
                  f_temp: float | None = None,
                  c_temp: float | None = None
                  ) -> dict[str, float | None]:
    ...
    result: dict[str, float | None] = {
        "c_temp": c_temp, "f_temp": f_temp
    }
    return result

def temperature_3(*,
                  f_temp: float | None = None,
                  c_temp: float | None = None
                  ) -> dict[str, float | None]:
    """Convert between Fahrenheit temperature and Celsius temperature.

    :key f_temp: Temperature in °F.
    :key c_temp: Temperature in °C.

    :returns: dictionary with two keys:
        :f_temp: Temperature in °F.
        :c_temp: Temperature in °C.
    """
    ...
    return {}

from typing import TypedDict
TempDict = TypedDict(
    "TempDict",
    {
        "c_temp": float,
        "f_temp": float
    }
)

def temperature_d(
        *,
        f_temp: float | None = None,
        c_temp: float | None = None
) -> TempDict:
    if f_temp is not None:
        c_temp = 5 * (f_temp - 32) / 9
    elif c_temp is not None:
        f_temp = 32 + 9 * c_temp / 5
    else:
        raise TypeError("One of t_temp or c_temp must be provided")
    result: TempDict = {"c_temp": c_temp, "f_temp": f_temp}
    return result

def temperature_bad(
    *,
    f_temp: float | None = None,
    c_temp: float | None = None
) -> float:

    if f_temp is not None:
        c_temp = 5 * (f_temp - 32) / 9
    elif f_temp is not None:
        f_temp = 32 + 9 * c_temp / 5
    else:
        raise TypeError("One of f_temp or c_temp must be provided")
    result = {"c_temp": c_temp, "f_temp": f_temp}
    return result

test_temperature = """
>>> temperature(f_temp=-13)
{'f_temp': -13, 'c_temp': -25.0}
>>> temperature_d(f_temp=-13)
{'c_temp': -25.0, 'f_temp': -13}
>>> temperature_d(c_temp=-25)
{'c_temp': -25, 'f_temp': -13.0}
"""

__test__ = {name: code for name, code in locals().items() if name.startswith("test_")}