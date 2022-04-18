from collections import Counter

s = int(input())

numbers = list(map(int, input().split()))

counter = Counter(numbers)

print(counter.most_common()[0][0])
