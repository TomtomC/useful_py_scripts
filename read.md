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
#For DECORATORS:
from decorators._retry import retry
from decorators._timing import get_time
from decorators._trycatch import try_catch, try_catch_retry

# For MODULES:
from modules._logs import log
```

## Help & Guidance

Always use @get_time above all other decorators.

For example:
```
@get_time
@trycatch(false)
...
```

## Version History
* 1.0.0.0
    * Initial commit
* 1.0.0.1
    * Include read.md file

## License
None - Copy the code and adjust for your own needs.

## Acknowledgments
Inspiration, code snippets, etc.
* [Indently](https://www.youtube.com/@Indently)
* (Contributors of StackOverflow, see comments in specific scripts)
