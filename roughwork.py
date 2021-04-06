from itertools import *
import os
import threading

# comb = permutations('ABCD',4)
# print([x for x in comb])

# print(f'Your current working directory is {os.getcwd()}')

# python_files = os.listdir()
# for values in python_files:
#     if 'zuri' in values:
#         print(values)
#
# print(threading.current_thread())



def sum(a:int,b:int)->int:
    """
    >>> print(sum(2,3))
    5

    >>> print(sum('a','b'))
    ab
    """
    return a+b

assert sum(2,3) == 5,'This should be 5'
if __name__ == '__main__':
    import doctest
    doctest.testmod()