
k = int(input())

even = k // 2
odd = k // 2 + 1 if k % 2 != 0 else k // 2
print(even * odd)
