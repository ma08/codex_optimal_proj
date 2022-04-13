from collections import Counter

def main():
    n = int(input())
    s = input()
    print(solve(s))

def solve(s):
    c = Counter(s)
    return c['A'] > c['D']

main()




l, r = [int(i) for i in input().split()]
if l == r and l > 0:
    print("Even", l*2)
elif l != r:
    print("Odd", max(l, r)*2)
else:
    print("Not a moose") 
