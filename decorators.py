"""Decorators"""
import time


def tictoc(func):
    def wrapper():
        start = time.perf_counter()
        func()
        func_time = time.perf_counter() - start
        print(f'{func.__name__} took {func_time} seconds')
    return wrapper


@tictoc
def say_hello():
    print('Decorators')
