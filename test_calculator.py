import calculator
import math
import pytest

@pytest.mark.parametrize("arg1, arg2, output", [(1, 2, 3), (2, 2, 4), (0, 3, 3), (0.34, 0.4, 0.74)] )
def test_add(arg1, arg2, output):
    assert calculator.add(arg1, arg2) == output

@pytest.mark.parametrize("arg1, arg2, output", [(2, 1, 2), (2, 2, 1), (6, 3, 2), (4, 0.5, 8)] )
def test_divide(arg1, arg2, output):
    assert calculator.divide(arg1, arg2) == output

@pytest.mark.parametrize("arg, output", [(1, 1), (2, 2), (3, 6), (5, 120), (0, 1)])
def test_factorial(arg, output):
    assert calculator.factorial(arg) == output

@pytest.mark.parametrize("arg, output", [(0, 0),
                                                (math.pi/4, float("{:.2f}". format((1/(math.sqrt(2)))))), 
                                                        (math.pi/2, round(1,2)), 
                                                            (3*math.pi/2, round(-1,2)) ] )
def test_sin(arg, output):
    assert calculator.sin(arg) == output


def test_is_float_raises_ValueError_for_string_arguments():
    with pytest.raises(ValueError):
        calculator.factorial(-1)
    with pytest.raises(TypeError):
        calculator.factorial(0.5)

def test_if_float_raises_ZeroDivisionError_for_values_divided_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3, 0)