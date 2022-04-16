

N = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)
print(sum(times))
