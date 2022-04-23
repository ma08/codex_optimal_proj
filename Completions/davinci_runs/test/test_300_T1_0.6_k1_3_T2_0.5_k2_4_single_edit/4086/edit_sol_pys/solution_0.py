

def main():
  n = int(input())
  a = [int(i) for i in input().split()]
  b = []
  for i in range(n):
    if a[i] not in b:
      b.append(a[i])
  print(len(b))
  print(*b, sep=' ')

main()
