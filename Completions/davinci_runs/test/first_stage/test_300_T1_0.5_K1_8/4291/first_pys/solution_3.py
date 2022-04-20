

N, Q = map(int, input().split())
S = input()

substrings = []
for i in range(N-1):
    if S[i:i+2] == "AC":
        substrings.append(i)

for i in range(Q):
    l, r = map(int, input().split())
    count = 0
    for s in substrings:
        if l-1 <= s <= r-2:
            count += 1
    print(count)