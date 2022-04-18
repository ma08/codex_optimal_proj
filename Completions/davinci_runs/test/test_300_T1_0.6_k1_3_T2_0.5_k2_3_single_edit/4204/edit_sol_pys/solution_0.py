
def get_digit(s,k):
    if k <= len(s): return s[k-1]
    for i,c in enumerate(s):
        k -= (int(c)*(10**(i+1)))
        if k <= 0:
            return str(int(c))[-1]

s = input()
k = int(input())

if len(s) == 1:
    print(s)
else:
    print(get_digit(s,k))
