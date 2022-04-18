

import sys
import math

n = int(sys.stdin.readline())
words = sys.stdin.readline().split()
if len(words) == n:
    if "mumble" in words:
        flag = 0
        count = 0
        for word in words:
            if word == "mumble":
                count += 1
            else:
                if int(word) != count + 1:
                    print("something is fishy")
                    flag = 1
                    break       
                else:
                    count += 1
        if count == n and flag == 0:
            print("makes sense")
    else:
        count = 0
        flag = 0
        for word in words:
            if int(word) != count + 1:
                print("something is fishy")
                flag = 1
                break   
            else:
                count += 1
        if count == n and flag == 0:
            print("makes sense")
else:
    print("something is fishy")
