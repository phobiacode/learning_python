"""Time"""

from time import perf_counter_ns


def get_time(function):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        func = function(*args, **kwargs)
        operation_time = perf_counter_ns() - start
        print(f'{function.__name__} took {operation_time} nanoseconds')
        return func
    return wrapper


"""Takes a string and returns the same string with every word that is 5 or more in length reversed"""


@get_time
def reversed_words(string):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in string.split())


print(reversed_words('What a beautiful day in the neighborhood'))



