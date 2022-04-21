

n = int(input())
a_list = list(map(int, input().split()))

if s == t:
    print(len(s))
else:
    print(len(s) + len(t) - 2 * len(set(s) & set(t)))
