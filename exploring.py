import numpy as np
from fractions import Fraction
import functools
import os
import psutil
import multiprocessing as mp


def get_cpu_percentage(target):
    period = 0.01  # 10 ms
    worker_process = mp.Process(target=target)
    worker_process.start()
    p = psutil.Process(worker_process.pid)

    # log cpu usage of `worker_process` every 10 ms
    while worker_process.is_alive():
        print(p.cpu_percent(period))


def how_much_cpu(func):
    """
    Utility to measure how much cpu percentage before and after execution of
    the decorated function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(get_cpu_percentage(func))

        result = func(*args, **kwargs)

        print(get_cpu_percentage(func))
        return result

    return wrapper


def do_stuff():
    for i in range(10000):
        for j in range(1000):
            x = 10 + i + j


do_stuff()
