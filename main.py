from decorators._timing import get_time
from decorators._trycatch import try_catch, try_catch_retry
from modules._logs import log
from time import sleep

#### AN EXAMPLE SCRIPT TO SHOWCASE THE DECORATORS AND MODULES ###


@get_time
@try_catch(False)
def test() -> int:
    log("info","delaying...")
    sleep(2)
    num = "test2"

    return int(num)

@get_time
@try_catch_retry(3, 1,False)
def connect() -> None:
    # pretend that this contains an actual sql connection
    sleep(1)
    raise Exception('Could not connect to internet...')

if __name__ == '__main__':
    log("info",f'Test Result = {test()}')
    connect()