
# solution

n = int(input())
t = input()

s = [0]*n

for i in range(n-1, 0, -1): # from n-1 to 1
  x = n//i
  y = n%i
  if y==0:
    for j in range(x): # x times
      s[i*j] = t[i*(x-1-j)] # i * (x-1-j) is the index of the last char in the j-th block
  else:
    for j in range(x+1): # x+1 times
      s[y+i*j] = t[y+i*(x-j)] # y+i*(x-j) is the index of the last char in the j-th block

print(''.join(s))
