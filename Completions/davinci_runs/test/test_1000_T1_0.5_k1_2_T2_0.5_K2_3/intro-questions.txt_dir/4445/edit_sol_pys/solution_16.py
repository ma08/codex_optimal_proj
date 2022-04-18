

n = int(input())
a = list(map(int, input().split()))

odd = [i for i in a if i % 2 == 1]
even = [i for i in a if i % 2 == 0]

if len(odd) % 2 == 0:
    odd.pop()

print(sum(odd) + sum(even))
