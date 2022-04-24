
def get_digit(s,k):
    if k <= len(s): return int(s[k-1])
    for i,c in enumerate(s):
        k -= (int(c)*(10**(i+1)))
        if k <= 0:
            return int(str(int(c))[-1])

def get_digits_sum(s,k):
    return sum([get_digit(s,i) for i in range(1,k+1)])

s = input()
k = int(input())

if len(s) == 1:
    print(int(s))
else:
    print(get_digits_sum(s,k))
