

n = int(input())
costumes = []
for i in range(n):
    costumes.append(input())

costume_freq = {}
for costume in costumes:
    if costume in costume_freq:
        costume_freq[costume] += 1
    else:
        costume_freq[costume] = 1

max_freq = max(costume_freq.values())
for costume in sorted(costume_freq):
    if costume_freq[costume] == max_freq:
        print(costume)
