

import sys

def name(n):
    if n == 1:
        return 'a'
    
    n -= 1
    letters = 'abcdefghijklmnopqrstuvwxyz'
    length = 1
    while True:
        if n < 26**length:
            break
        n -= 26**length
        length += 1
    
    name = ''
    while length > 0:
        name += letters[n // 26**(length - 1)]
        n %= 26**(length - 1)
        length -= 1
    
    return name

n = int(sys.stdin.readline().rstrip())
print(name(n))