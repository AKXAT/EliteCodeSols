"""Test Solution for concatenation of array."""
import logging

import pytest
from assets import decorator

from Solutions.concatenation_of_array import Solution

mylogger = logging.getLogger()


@decorator.testdecorator
def test_concatenation_of_array():
    """First Test."""
    input = [1, 2, 1]
    result = [1, 2, 1, 1, 2, 1]
    mylogger.info(f"Checking for {input}")
    solution_object = Solution()
    mysolution = solution_object.getConcatenation(input)
    assert mysolution == result, "Test failed, the solution is not correct."
    assert len(mysolution) == 2 * (
        len(input)
    ), "Solution length is not 2 times the length of input."
