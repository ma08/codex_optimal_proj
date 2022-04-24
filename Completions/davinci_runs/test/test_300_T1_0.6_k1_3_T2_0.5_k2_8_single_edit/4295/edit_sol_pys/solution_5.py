

"""
-----TODO-----
-
"""

"""
-----Solution-----
"""

# This code is for the purpose of importing faster input/output methods.
import atexit
import io
import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).next
_OUTPUT_BUFFER = io.BytesIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Your code goes here.

N, K = map(int, input().split()) # input() is a faster input method.

if N % K == 0:
    print(0)
else:
    print(min(N % K, K - N % K))
