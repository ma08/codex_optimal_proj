
import sys

n = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]

sum_of_inverses = 0
for number in numbers:
    sum_of_inverses += 1.0 / number

print(1.0 / sum_of_inverses)
