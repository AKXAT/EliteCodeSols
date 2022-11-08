"""Test Solution for running sum of array."""
import logging

import pytest
from assets import decorator

from Solutions.running_sum_of_array import Solution

mylogger = logging.getLogger()


@decorator.testdecorator
def test_running_sum_array():
    """First Test."""
    input = [1, 2, 3, 4]
    result = [1, 3, 6, 10]
    mylogger.info(f"checking for input {input}")
    solution_obj = Solution()
    mysolution = solution_obj.runningSum(input)
    assert mysolution == result, "Test failed for running sum array."
