
n = int(input())
costume = []
for i in range(n):
    costume.append(input())

costume_frequency = {}
for costume in costume:
    if costume in costume_frequency:
        costume_frequency[costume] += 1
    else:
        costume_frequency[costume] = 1

max_frequency = max(costume_frequency.values())
for costume in sorted(costume_frequency):
    if costume_frequency[costume] == max_frequency:
        print(costume)
