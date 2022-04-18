#
# import sys
#
# def main():
#     n = int(sys.stdin.readline())
#     t = list(map(int, sys.stdin.readline().split()))
#     t.sort()
#     print(sum(t[i]*(n-i) for i in range(n))) # t[i]*(n-i) is the waiting time for the ith customer
#
# main()


import math

def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

print(is_prime(1))
