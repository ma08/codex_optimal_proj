

n = int(input())
numbers = [int(x) for x in input().split()]

sum_of_inverses = 0.0
for number in numbers:
    sum_of_inverses += 1/number

print(1/sum_of_inverses)
