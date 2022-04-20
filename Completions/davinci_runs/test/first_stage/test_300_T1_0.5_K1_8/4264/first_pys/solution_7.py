

n = int(input())

# count the number of positive integers less than or equal to n that have an odd number of digits
count = 0
for i in range(1, n+1):
    if len(str(i)) % 2 == 1:
        count += 1

print(count)