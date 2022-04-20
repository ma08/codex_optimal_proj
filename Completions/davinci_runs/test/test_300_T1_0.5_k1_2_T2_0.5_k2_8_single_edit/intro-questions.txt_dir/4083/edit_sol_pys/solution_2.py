
n, k = [int(i) for i in raw_input().split()]
a = [int(i) for i in input().split()]
print(max(a) - min(a) - k + 1)
