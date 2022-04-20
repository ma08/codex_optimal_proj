# coding: utf-8


import sys
import io
import time
import pprint

input = sys.stdin.readline

# copy the below part and paste to the submission form.
# ---------function------------
import math


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()

    ans = a_list[0]
    for a in a_list:
        ans = math.gcd(ans, a)

    print(ans)


main()
# -----------------------------
sys.stdin = io.StringIO('''
4
1 2 3 4
''')
start = time.time()
# copy the above part and paste to the submission form.
# ---------function------------
import math


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()

    ans = a_list[0]
    for a in a_list:
        ans = math.gcd(ans, a)

    print(ans)


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
