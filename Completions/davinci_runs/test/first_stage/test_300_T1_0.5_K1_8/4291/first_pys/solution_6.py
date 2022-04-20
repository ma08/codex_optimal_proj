

# AC
n, q = map(int, input().split())
s = input()

ac_dict = {}

for i in range(n):
    if s[i:i+2] == 'AC':
        ac_dict[i] = 1

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    cnt = 0
    for i in ac_dict:
        if i >= l and i < r:
            cnt += 1
    print(cnt)