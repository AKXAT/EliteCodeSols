"""Test solution for final value variable after performing operations."""

import logging

import pytest
from assets import decorator

from Solutions.final_value_variable_after_operation import Solution

mylogger = logging.getLogger()


@decorator.testdecorator
def test_final_value_after_operations():
    """First test."""
    input = ["--X", "X++", "X++"]
    result = 1
    mylogger.info(f"checking for input {input}")
    solution_obj = Solution()
    mysolution = solution_obj.finalValueAfterOperations(input)
    assert mysolution == result, "Test failed for running final value after operations."


@decorator.testdecorator
def test_final_value_after_operations_2():
    """First test."""
    input = ["++X", "++X", "X++"]
    result = 3
    mylogger.info(f"checking for input {input}")
    solution_obj = Solution()
    mysolution = solution_obj.finalValueAfterOperations(input)
    assert mysolution == result, "Test failed for running final value after operations."
