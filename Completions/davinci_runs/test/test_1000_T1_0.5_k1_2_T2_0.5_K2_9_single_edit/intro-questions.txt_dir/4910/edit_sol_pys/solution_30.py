
N = int(input())
costumes = [input() for i in range(N)]

costume_freq = {}
for costume in costumes:
    costume_freq[costume] = costume_freq.get(costume, 0) + 1

max_freq = max(costume_freq.values())
for costume in sorted(costume_freq):
    if costume_freq[costume] == max_freq:
        print(costume)
