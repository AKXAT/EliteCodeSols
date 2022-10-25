"""Test Decorator."""
import logging
import time
from datetime import timedelta

mylogger = logging.getLogger()
from assets import decorator


@decorator.testdecorator
def testdecorator(func):
    """Outer Function."""

    def wrapper():
        """Inner Function."""
        start_time = time.monotonic()
        mylogger.info("------------------> TEST START  <------------------")
        mylogger.info(f"Running Test for => {func.__name__}")
        end_time = time.monotonic()
        mylogger.info(
            f" Time Take for execution => {timedelta(seconds=end_time - start_time).microseconds}"
        )
        mylogger.info("-------------------> TEST END  <-------------------")
