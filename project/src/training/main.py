import typing

"""
Note that the typing is just hints to the IDE and the human, and have no bearing on runtime.
"""

def get_div_and_remainder(number: int, divisor: int) -> tuple[int, int]:
    return (number // divisor, number % divisor)

def convert_to_roman_numeral(number: int) -> str:
    return 'I' * number
