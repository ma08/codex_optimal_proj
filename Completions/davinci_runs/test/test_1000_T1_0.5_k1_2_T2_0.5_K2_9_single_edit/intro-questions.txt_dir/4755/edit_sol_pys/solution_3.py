

c, k = map(int, input().split())
print(c - c % 10 ** k + 10 ** k if c % 10 ** k >= 5 * 10 ** (k - 1)
      else c - c % 10 ** k)
