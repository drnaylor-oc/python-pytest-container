import pytest
import training.main as t

def standard_test():
    """
    A standard test that runs as part of the test suite -- no markers required
    """
    assert 1 == 1

@pytest.mark.parametrize("test_input,expected", 
                         [(1, "I"), 
                          (2, "II"), 
                          (3, "III")])
def test_conversion(test_input: int, expected: str):
    """
    Tests that the roman numeral function works as expected, uses parameterised tests.
    """
    assert t.convert_to_roman_numeral(test_input) == expected

@pytest.mark.parametrize("number,divisor,quotient,remainder", 
                         [(1, 1, 1, 0), 
                          (2, 1, 2, 0), 
                          (3, 2, 1, 1)])
def test_division(number, divisor, quotient, remainder):
    assert t.get_div_and_remainder(number, divisor) == (quotient, remainder)

