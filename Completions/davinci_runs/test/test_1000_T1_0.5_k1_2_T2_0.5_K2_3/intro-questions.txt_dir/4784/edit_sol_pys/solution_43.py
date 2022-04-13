"""
>>> X = int(input())
>>> N = int(input())
>>> total_used = 0
>>> for i in range(N):
...     used = int(input())
...     total_used += used
...
>>> print(X + total_used)
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
