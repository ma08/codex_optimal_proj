

import sys
import math

n = int(sys.stdin.readline())
words = sys.stdin.readline().split()

if len(words) == n:
    if "mumble" in words:  # if there is a "mumble" in words
        count = 0
        for word in words:  # loop through the words
            if word == "mumble":
                count += 1  # if word is "mumble" then count += 1
            else:
                if int(word) != count + 1:  # if word is not "mumble" then check if the word is equal to count + 1
                    print("something is fishy")
                    break
                else:
                    count += 1
        if count == n:  # if count is equal to n then it makes sense
            print("makes sense")
    else:
        count = 0
        for word in words:  # loop through the words
            if int(word) != count + 1:  # if word is not equal to count + 1 then it is something fishy
                print("something is fishy")
                break
            else:
                count += 1
        if count == n:  # if count is equal to n then it makes sense
            print("makes sense")
else:
    print("something is fishy")


























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































