

# input
n = int(input())

# the minimum positive integer divisible by both 2 and n
answer = n

# if n is even, then n is divisible by both 2 and n
while answer % 2 != 0:
    answer += n

print(answer)
