

n = int(input())
a_list = list(map(int, input().split()))

a_list.sort()

print(a_list[n//2] - a_list[n//2-1])
