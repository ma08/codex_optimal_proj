

import math
import sys

n = int(input())

def get_name(n):
    if n < 27:
        return chr(ord('a') + n - 1)
    else:
        base = 26
        while n > base:
            n -= base
            base = 26 * base
        return get_name(n // 26) + get_name(n % 26)

print(get_name(n))