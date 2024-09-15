from time import perf_counter, perf_counter_ns, sleep
from functools import wraps
from typing import Callable, Any
from modules._logs import log

# IMPORTANT!! This decorator relies on _logs.py in the modules folder

"""
!!!!! VERY IMPORTANT !!!!!
Place the get_time decorator above all other decorators you may use for a function.
If you put get_time under another decorator, it will either throw and error or produce no result.
"""

# =======================CODE=======================

def get_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # This is a very basic module for timing functions
        # The timeit module will be far more accurate for timing whole blocks of code.

        # settings //  change these if you prefer the nanosecond counter or a different number of decimal places.
        timer_type: str = "default" # change this is ns for nanosecond counter
        decimal_places: int = 3

        # default values to make pycharm happy
        end_t: float = 0
        start_t: float = 0
        count_type: str = "seconds"

        # default = seconds
        # ns = nanoseconds
        # trigger default is incorrect value used. No need for error triggering,
        if timer_type == "default" or (timer_type != "default" and timer_type != "ns"):
            start_t = perf_counter()
            result: Any = func(*args, **kwargs)
            end_t = perf_counter()
            count_type = "seconds"

        elif timer_type == "ns":
            start_t = perf_counter_ns()
            result: Any = func(*args, **kwargs)
            end_t = perf_counter_ns()
            count_type = "nanoseconds"

        log("info",f'"{func.__name__}()" took {end_t - start_t:.{str(decimal_places)}f} {count_type} to execute')
        return result

    return wrapper


# =======================TEST=======================
# @get_time
# def connect() -> None:
#     print('Connecting...')
#     sleep(1) # brrr, pretend sql stuff
#     print('Connected!')
#
# @get_time
# def a_lotta_loops() -> None:
#     many_loops: int = int(47483647)
#
#     print('Looping...')
#     for n in range(many_loops):
#         pass
#
#     print('Done looping!')
#
#
# def main() -> None:
#     a_lotta_loops()
#     connect()
#
#
# if __name__ == '__main__':
#     main()