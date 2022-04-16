
# @Author: aaronmishkin
# @Email:  amishkin@cs.ubc.ca

# MIT License
# Copyright (c) 2017 Aaron Mishkin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math

# This is a binary search solution to the problem.

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

def pack(a, k, m, l):
    res = 0
    j = 0
    for i in range(l):
        if j >= len(a):
            break
        while j < len(a) and a[j] <= k and i < l:
            i += 1
            k -= a[j]
            j += 1
            res += 1
        k = m - (l - i)
    return res

l = 0
r = n
while l < r:
    mid = (l + r) // 2
    if pack(a[:mid], k, m, mid) < mid:
        l = mid + 1
    else:
        r = mid
print(l)
