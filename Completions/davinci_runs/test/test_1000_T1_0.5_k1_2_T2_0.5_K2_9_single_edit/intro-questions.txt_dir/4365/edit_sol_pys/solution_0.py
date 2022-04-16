

k = int(input())

even_count = k // 2
odd_count = k // 2 + 1 if k % 2 != 0 else k // 2



a, b, c = map(int, input().split())

print(a * b * c)


n = int(input())

print(n * (n + 1) // 2)
print(even_count * odd_count)
