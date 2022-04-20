

# SOLUTION

n = int(input())
s = input()
t = input()

def swap(s,i):
  return s[:i]+s[i+1]+s[i]+s[i+2:]

def get_swaps(s,t):
  if s == t:
    return []
  for i in range(n-1):
    if s[i] != t[i]:
      if s[i+1] == t[i]:
        return [i+1] + get_swaps(swap(s,i+1),t)
      else:
        return [i] + get_swaps(swap(s,i),t)
  return [-1]

swaps = get_swaps(s,t)
if swaps[0] == -1:
  print(-1)
else:
  print(len(swaps))
  print(*swaps)