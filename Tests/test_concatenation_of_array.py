"""Test Solution for concatenation of array."""
import logging
from importlib.abc import TraversableResources

import pytest
from assets import decorator

from Solutions.concatenation_of_array import Solution

mylogger = logging.getLogger()


@decorator.testdecorator
def test_concatenation_of_array():
    """First Test."""
    assert True
