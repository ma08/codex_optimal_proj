

# Translation
trans_dict = {}

# Input
m, n = [int(x) for x in input().split()]
for _ in range(m):
    a, b = input().split()
    if a not in trans_dict:
        trans_dict[a] = []
    trans_dict[a].append(b)

for _ in range(n):
    w1, w2 = input().split()
    if len(w1) != len(w2):
        print('no')
        continue
    # Check if words match
    for a, b in zip(w1, w2):
        if a in trans_dict:
            if b not in trans_dict[a]:
                print('no')
                break
        elif a != b:
            print('no')
            break
    else:
        print('yes')