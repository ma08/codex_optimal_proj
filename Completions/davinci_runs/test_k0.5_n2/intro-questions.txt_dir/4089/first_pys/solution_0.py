

import math
N = int(input())

def calc_digits(n):
    return math.ceil(math.log(n+1, 26))

def calc_index(n, digits):
    return n - 26**(digits-1)

def calc_char(n):
    return chr(n+97)

digits = calc_digits(N)
index = calc_index(N, digits)

ans = ""
for i in range(digits-1, -1, -1):
    num = math.floor(index/26**i)
    ans += calc_char(num)
    index -= num*26**i
print(ans)