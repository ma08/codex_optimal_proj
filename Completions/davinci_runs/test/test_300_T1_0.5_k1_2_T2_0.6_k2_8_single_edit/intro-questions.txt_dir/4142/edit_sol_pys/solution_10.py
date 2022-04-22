
#
s = list(input())

n = len(s)

odds = [s[i] for i in range(n) if i % 2 == 0]
evens = [s[i] for i in range(n) if i % 2 == 1]

if all(x in ['R', 'U', 'D'] for x in odds) and all(x in ['L', 'U', 'D'] for x in evens):
    print("Yes")
else:
    print("No")
