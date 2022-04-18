
n = int(input())
s = input()

print(sum([i - 1 for i in Counter(s).values()]))
