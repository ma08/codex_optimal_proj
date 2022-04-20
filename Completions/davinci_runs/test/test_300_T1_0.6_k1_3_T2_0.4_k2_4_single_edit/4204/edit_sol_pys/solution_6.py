
def get_digit(s,k):
    if k <= len(s): return int(s[k-1])
    for i,c in enumerate(s):
        k -= (int(c)*(10**(i+1)))
        if k <= 0:
            return int(str(int(c))[-1])

def get_digit_sum(s):
    return sum([get_digit(s,k) for k in range(1,len(s)+1)])

s = input()
k = int(input())

if len(s) == 1:
    print(int(s))
else:
    print(get_digit_sum(s))
