

n = int(input())
a = list(map(int, input().split()))

def solve(n, a):
    prefix_sum = [0]
    for i in a:
        prefix_sum.append(prefix_sum[-1] + i)
    prefix_sum = prefix_sum[1:]
    prefix_sum_set = set()
    for i in prefix_sum:
        if i in prefix_sum_set:
            return 1
        prefix_sum_set.add(i)
    return 0

print(solve(n, a))