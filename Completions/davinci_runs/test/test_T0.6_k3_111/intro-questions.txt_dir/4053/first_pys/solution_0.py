

n = int(input())
prefixes = []
suffixes = []
for i in range(2*n-2):
  s = input()
  if len(s) == 1:
    prefixes.append(s)
    suffixes.append(s)
  else:
    prefixes.append(s[:-1])
    suffixes.append(s[1:])

ans = []
for i in range(2*n-2):
  if prefixes[i] not in prefixes[:i] and prefixes[i] not in suffixes[:i]:
    ans.append("P")
  else:
    ans.append("S")

print("".join(ans))