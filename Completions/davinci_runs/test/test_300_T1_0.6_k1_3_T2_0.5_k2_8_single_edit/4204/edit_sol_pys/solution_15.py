from math import log

def get_digit(s,k):
    if k <= len(s): return s[k-1]

    for i,c in enumerate(s):
        k -= (int(c)*(10**(i+1))) # get the kth digit
        if k <= 0:
            return str(int(c))[-1]

s = input()
k = int(input())

print(get_digit(s,k))
