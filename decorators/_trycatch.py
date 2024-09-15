import time
from functools import wraps as wraps
from typing import Callable, Any
from time import sleep
from modules._logs import log as log

# IMPORTANT!! This decorator relies on _logs.py in the modules folder

# =======================CODE=======================
def try_catch(rethrow: bool = False) -> Callable:
    """
    Attempt to call a function, if it fails, trigger an error log.
    Option added to rethrow and stop the python script completely

    :param rethrow: TRUE = rethrow the exception and exit script, FALSE = continue the script
    :return:
    """

    def trying(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:

            try:
                log("info", f'Running: {func.__name__}()')
                return func(*args,**kwargs)
            except Exception as ex:
                if rethrow:
                    log("critical", f'{repr(ex)}.')
                    log("critical", f'"{func.__name__}()" failed...')
                    raise
                log("error",str(ex))
            finally:
                if not rethrow:
                    log("info",f'"{func.__name__}()" done...')

        return wrapper
    return trying

def try_catch_retry(retries: int = 1, delay: float = 1, rethrow: bool = False) -> Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.
    Option added to rethrow and stop the python script completely

    :param retries: The max amount of retries you want for the function call
    :param delay: The delay (in seconds) between each function retry
    :param rethrow: TRUE = rethrow the exception and exit script, FALSE = continue the script and retry function
    :return:
    """

    # check to ensure that values are not 0
    if retries < 1 or delay <= 0:
        raise ValueError('Retry number <1 or delay time <=0.')

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive

                try:
                    log("info",f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e: # general exception is easier than writing out each individual exception type.
                    # break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        if rethrow:
                            log("critical", f'{repr(e)}.')
                            log("critical", f'"{func.__name__}()" failed...')
                            raise
                        log("error",f'Error: {repr(e)}.')
                        log("error",f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        log("error",f'{repr(e)} -> Retrying...')
                        sleep(delay)  # Add a delay before running the next iteration
                finally:
                    if not rethrow:
                        log("info", f'"{func.__name__}()" done...')

        return wrapper

    return decorator

# # =======================TEST=======================
#
# retry_num: int = 3
# retry_delay: float = 1
#
# @try_catch(True)
# def test() -> None:
#     raise Exception("Hello World")
#
# @try_catch_retry(retry_num, retry_delay,False)
# def connect() -> None:
#     # pretend that this contains an actual sql connection
#     time.sleep(1)
#     raise Exception('Could not connect to internet...')
#
# # testing without in_argument variables assigned
# @try_catch_retry()
# def connect_again() -> None:
#     # pretend that this contains an actual sql connection
#     time.sleep(1)
#     raise Exception('Could not connect to internet...')
#
#
# def main() -> None:
#     print(f'Retries = {str(retry_num)}')
#     print(f'Delay = {str(retry_delay)}')
#     connect()
#     connect_again()
#     test() # decorator is set to true (see above) - this will deliberately rethrow the error to force a script exit
#
#
# if __name__ == '__main__':
#     main()