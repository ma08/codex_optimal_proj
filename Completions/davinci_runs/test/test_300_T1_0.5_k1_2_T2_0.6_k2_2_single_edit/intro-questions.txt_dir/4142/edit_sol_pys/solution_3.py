
s = input()

n = len(s)

odds = [int(x) for i, x in enumerate(s) if i % 2 == 0]
evens = [int(x) for i, x in enumerate(s) if i % 2 == 1]

print(sum(odds) * sum(evens))
