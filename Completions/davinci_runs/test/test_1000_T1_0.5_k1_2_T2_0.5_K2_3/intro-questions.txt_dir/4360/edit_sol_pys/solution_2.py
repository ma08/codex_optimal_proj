
import sys

n = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]

sum_of_inverses = 0
for num in numbers:
    sum_of_inverses += 1/num

print(1/sum_of_inverses)
