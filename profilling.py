import functools
import os
from time import time
import psutil


def print_memory_usage():
    """Prints current memory usage in mega bytes"""
    pid = os.getpid()
    ps = psutil.Process(pid)
    memory_usage = ps.memory_info()
    print(f'{memory_usage.rss / 1024**2} mb')


class Timer:
    """Utility to be used as a context manager to calculate time execution"""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.finish = time.perf_counter()
        print(f'Time elapse {self.finish - self.start:0.4f} s')


def timer(func):
    """Utility to calculate time execution as a decorator"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        finish = time.perf_counter()

        print(f'Elapsed time: {finish - start:0.4f} s')
        return value

    return wrapper
