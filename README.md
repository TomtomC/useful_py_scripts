# Useful .py Scripts

A repository containing useful .py scripts for python projects.

## Description

The purpose of this repository is to contain some .py scripts that can be re-used for any python project you're
working on.

## Getting Started

### Dependencies

* Python 3.12 and above (using earlier versions may still work)
* Packages used:
  * logger
  * json
  * functools
  * typing
  * time

### Installing

* Fork this repo and/or download the contents onto your local PC.
* Copy the 'decorator' and 'modules' folders into your python project.

### Executing scripts

Copy the below to install all active functions into your project.
Do tailor the imports to what you actually need.
  
```
# For MODULES:
from modules._logs import log

#For DECORATORS:
from decorators._timing import get_time
from decorators._trycatch import try_catch, try_catch_retry
```
//////////////////////////////////////////
#### log
//////////////////////////////////////////

!!! @log is used in all scripts in this repo. Please take note of this if you wish to adjust the scripts yourself !!!

The log function uses the logger package's JSON configuration setup. The settings.json file in the modules folder can
be adjusted to change the logging output. By default, all outputs will be saved to a **log.txt** file.

The below example has all the possible log options you can use:
```
def main() -> None:
    log("info","Hello World")
    log("warning","Hello World")
    log("error","Hello World")
    log("critical","Hello World")
    log("debug","Hello World")

if __name__ == '__main__':
    main()
```

And an example of the outputs. 
```
2024-Sep-15 12:17:11 [INFO    ] Hello World
2024-Sep-15 12:17:11 [WARNING ] Hello World
2024-Sep-15 12:17:11 [ERROR   ] Hello World
NoneType: None
2024-Sep-15 12:17:11 [CRITICAL] Hello World
NoneType: None

Process finished with exit code 0
```
Both ERROR and CRITICAL type logs will produce the full breakdown of the exception if placed within an exception check.
Please also refer to the **@try_catch** and **@try_catch_retry** scripts to see examples.

===

For assistance with adjusting the setting.json file, refer to the following documentations:

[The Offical Logger Documentation](https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema)

[Useful StackOverflow Page](https://stackoverflow.com/questions/7507825/where-is-a-complete-example-of-logging-config-dictconfig)

[Additional Info](https://realpython.com/python-logging/)


//////////////////////////////////////////
#### get_time
//////////////////////////////////////////

To log the time of your function, use get_time(). Results will be in seconds

```
@get_time()
def your_func_code() -> None:
  print(int("Hello World"))
```

//////////////////////////////////////////
#### try_catch_retry
//////////////////////////////////////////

As per the name, this decorator will retry the function if an error occurs.

The default values are as follows:
* Number of retries = 1
* Delay before next retry = 1 second
* Rethrow error = FALSE
These can be adjusted within the decorator, using 4 retries, a two-second delay
and no rethrowing of the error, using the below example:
```
@try_catch_retry(4,2,False)
def your_func_code() -> None:
  print(int("Hello World"))
  
your_func_code()

### output:
# 
# ... below is last retry output
#
# 2024-Sep-15 12:01:42 [INFO    ] Running (4): your_func_code()
# 2024-Sep-15 12:01:42 [ERROR   ] Error: ValueError("invalid literal for int() with base 10: 'Hello World'").
# Traceback (most recent call last):
#  File "C:\Users\User\PycharmProjects\useful_py_scripts\decorators\_trycatch.py", line 61, in wrapper
#    return func(*args, **kwargs)
#           ^^^^^^^^^^^^^^^^^^^^^
#  File "C:\Users\User\PycharmProjects\useful_py_scripts\decorators\_trycatch.py", line 94, in your_func_code
#    print(int("Hello World"))
#          ^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'Hello World'
# 2024-Sep-15 12:01:42 [ERROR   ] "your_func_code()" failed after 4 retries.
# Traceback (most recent call last):
#  File "C:\Users\User\PycharmProjects\useful_py_scripts\decorators\_trycatch.py", line 61, in wrapper
#    return func(*args, **kwargs)
#           ^^^^^^^^^^^^^^^^^^^^^
#  File "C:\Users\User\PycharmProjects\useful_py_scripts\decorators\_trycatch.py", line 94, in your_func_code
#    print(int("Hello World"))
#          ^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'Hello World'
# 2024-Sep-15 12:01:42 [INFO    ] "your_func_code()" done...
```

//////////////////////////////////////////
#### try_catch
//////////////////////////////////////////

This is a basic try-catch function.

If you want an error to be logged, but the script to continue:
```
@try_catch(False)
def your_func_code():
  print(int("Hello World"))
```

If you want an error to be logged, but the script to exit upon the error:
```
@try_catch(True)
def your_func_code():
  print(int("Hello World"))
```
Error results are logged in the same way as try_catch_retry


## Help & Guidance

* Always use @get_time above all other decorators. 
  
  For example:
  ```
  @get_time
  @trycatch(false)
  ...
  ```

* @get_time will produce an approx. time for functions. Do not use this for extremely accurate time results.

## Version History
* 1.0.0.0
    * Initial commit
* 1.0.0.1
    * Include read.md file
* 1.0.0.2
    * Expanded details about decorator and module functions.

## License
None - Copy the code and adjust for your own needs.

## Acknowledgments
Inspiration, code snippets, etc.
* [Indently](https://www.youtube.com/@Indently)
* StackOverflow contributors
