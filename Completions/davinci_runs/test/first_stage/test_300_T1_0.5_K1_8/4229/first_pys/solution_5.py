

n = int(input())

sum_fizzbuzz = 0
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        sum_fizzbuzz += i
    elif i % 3 == 0:
        sum_fizzbuzz += i
    elif i % 5 == 0:
        sum_fizzbuzz += i
    else:
        sum_fizzbuzz += i

print(sum_fizzbuzz)