

import sys
import math


n = int(sys.stdin.readline())
words = sys.stdin.readline().split()  # readline() reads the whole line

if len(words) == n:
    if "mumble" in words:
        if words.index("mumble") == n - 1:
            print("makes sense")  # if mumble is the last word
        else:
            print("something is fishy")
    else:
        if int(words[n - 1]) == n:
            print("makes sense")  # if last word is the last number
        else:
            print("something is fishy")
else:
    print("something is fishy")  # if the number of words is not n
