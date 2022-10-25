"""Test Solution  for Build Array from Permutation."""
import logging

import pytest
from assets import decorator

from Solutions.build_array_from_permutation import Solution

mylogger = logging.getLogger()


@decorator.testdecorator
def test_build_array_from_permutation():
    """First Test."""
    input_array = [0, 2, 1, 5, 3, 4]
    result_array = [0, 1, 2, 4, 5, 3]
    mylogger.info(f"Checking for = {input_array}")
    solution_object = Solution()
    mysolution = solution_object.buildArray(nums=input_array)
    mylogger.info(f"The result is = {mysolution}")
    assert mysolution == result_array, "Test Failed for Build Array from Permutation"
