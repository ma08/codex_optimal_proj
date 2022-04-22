

N = int(input())

odd_count = 0
if N % 2 == 0:
    odd_count = N // 2
else:
    odd_count = N // 2 + 1

print(odd_count)
