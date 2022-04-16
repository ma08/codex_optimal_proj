

s = list(input())

n = len(s)

if all(x in ['R', 'U', 'D'] for x in odds) and all(x in ['L', 'U', 'D'] for x in evens):
    print("Yes")
else:
    print("No")
