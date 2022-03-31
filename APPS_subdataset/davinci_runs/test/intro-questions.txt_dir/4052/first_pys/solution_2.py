

#-----Solution-----

s = input()
str1 = input()
str2 = input()

def swap(str, i, j):
  str = list(str)
  temp = str[i]
  str[i] = str[j]
  str[j] = temp
  return ''.join(str)

def swapchar(str1, str2):
  cnt = 0
  flag = True
  while flag:
    flag = False
    for i in range(len(str1)):
      if str1[i] != str2[i]:
        for j in range(i+1, len(str1)):
          if str1[j] == str2[i]:
            str1 = swap(str1, i, j)
            cnt += 1
            flag = True
            break
        if flag:
          break
  if str1 != str2:
    return -1
  return cnt

n = swapchar(str1, str2)
print(n)
if n == -1:
  print(-1)
else:
  for i in range(n):
    print(i+1, end=' ')