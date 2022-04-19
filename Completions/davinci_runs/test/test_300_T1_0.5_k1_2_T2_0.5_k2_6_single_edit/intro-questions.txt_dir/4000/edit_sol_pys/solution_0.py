


n = int(input())
a = list(map(int, input().split()))

ones_count = a.count(1)
zeros_count = n - ones_count

if zeros_count >= ones_count:
    print(n - ones_count)
else:
    print(zeros_count)
