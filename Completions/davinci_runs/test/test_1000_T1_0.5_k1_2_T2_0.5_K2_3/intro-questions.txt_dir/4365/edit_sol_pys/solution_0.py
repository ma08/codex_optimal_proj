

n = int(input())

even_count = n // 2 + 1 if n % 2 != 0 else n // 2
odd_count = n // 2

print(even_count * odd_count)
