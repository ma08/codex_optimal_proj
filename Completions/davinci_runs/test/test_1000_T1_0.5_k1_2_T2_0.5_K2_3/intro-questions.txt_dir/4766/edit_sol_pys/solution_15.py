# Simon says

import sys

for _ in range(int(input())):
    if input().startswith("Simon says"):
        print(input())
    else:
        print(0)
