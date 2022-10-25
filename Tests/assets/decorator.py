"""Test Decorator."""
import logging
import time
from datetime import timedelta

from assets import decorator

mylogger = logging.getLogger()


def testdecorator(func):
    """Outer Function."""

    def wrapper():
        """Inner Function."""
        start_time = time.monotonic()
        mylogger.info("------------------> TEST START  <------------------")
        mylogger.info(f"Running Test for => {func.__name__}")
        func()
        end_time = time.monotonic()
        mylogger.info(
            f" Time Take for execution => {timedelta(seconds=end_time - start_time).microseconds} Microseconds"
        )
        mylogger.info("-------------------> TEST END  <-------------------")

    return wrapper
