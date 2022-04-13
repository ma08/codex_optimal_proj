
# Translations
translations = {}

# Input
m, n = [int(x) for x in input().split()]
for _ in range(m):
    a, b = input().split()
    if a not in translations:
        translations[a] = []
    translations[a].append(b)

for _ in range(n):
    w1, w2 = input().split()
    if len(w1) != len(w2):
        print('no')
        continue
    # Check if words match
    for a, b in zip(w1, w2):
        if a in translations:
            if b not in translations[a]:
                print('no')
                continue
        elif a != b:
            print('no')
            continue
    else:
        print('yes')
