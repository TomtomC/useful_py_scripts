import time
from functools import wraps as wraps
from typing import Callable, Any
from time import sleep
from modules._logs import log

# IMPORTANT!! This decorator relies on _logs.py in the modules folder

# =======================CODE=======================
# default settings
retry_num: int = 3
retry_delay: float = 1

def retry(retries: int = retry_num, delay: float = retry_delay) -> Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.

    :param retries: The max amount of retries you want for the function call
    :param delay: The delay (in seconds) between each function retry
    :return:
    """

    # Don't let the user use this decorator if they are high
    if retries < 1 or delay <= 0:
        raise ValueError('Retry number <1 or delay time <=0.')

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive

                try:
                    log("info",f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        log("error",f'{repr(e)}.')
                        log("error",f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        log("warning",f'{repr(e)} -> Retrying...')
                        sleep(delay)  # Add a delay before running the next iteration

        return wrapper

    return decorator

# =======================TEST=======================
@retry(retry_num, retry_delay)
def connect() -> None:
    # pretend that this contains an actual sql connection
    time.sleep(1)
    raise Exception('Could not connect to internet...')

# testing without in_argument variables assigned
@retry()
def connect_again() -> None:
    # pretend that this contains an actual sql connection
    time.sleep(1)
    raise Exception('Could not connect to internet...')


def main() -> None:
    print(f'Retries = {str(retry_num)}')
    print(f'Delay = {str(retry_delay)}')
    connect()
    connect_again()


if __name__ == '__main__':
    main()