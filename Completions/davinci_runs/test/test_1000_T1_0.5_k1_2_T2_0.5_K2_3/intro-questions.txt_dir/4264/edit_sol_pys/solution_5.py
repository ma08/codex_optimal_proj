n = int(input())

odd_count = 0
for i in range(1, n + 1):
    if len(str(i)) % 2 == 1:
        odd_count += 1

print(odd_count)
