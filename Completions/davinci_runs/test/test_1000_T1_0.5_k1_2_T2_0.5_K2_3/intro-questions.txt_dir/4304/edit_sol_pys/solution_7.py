

import sys

a, b = map(int, sys.stdin.readline().rstrip().split()) # map(function, iterable, ...)
                                                      # return an iterator that applies function to every item of iterable,
                                                      # yielding the results.
                                                      # if additional iterable arguments are passed,
                                                      # function must take that many arguments and is applied to the items
                                                      # from all iterables in parallel.
                                                      # with multiple iterables, the iterator stops when the shortest iterable
                                                      # is exhausted.
                                                      # map() is equivalent to [function(x) for x in iterable]. map() is useful
                                                      # when you need to apply a transformation function to each item in an
                                                      # iterable and transform them into a new iterable.

if a == 1:
    print(b - a)
else:
    print(b - a - 1)
