
from operator import itemgetter

def get_max_possible_sum(numbers):
    numbers.sort(key=itemgetter(1), reverse=True)
    return sum(number[1] for number in numbers[:k])

a, b, c, k = map(int, input().split())
numbers = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(numbers))
