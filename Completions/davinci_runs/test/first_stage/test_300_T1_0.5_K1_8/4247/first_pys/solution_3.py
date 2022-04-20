

n = int(input())
p_list = [int(i) for i in input().split()]

count = 0

for i in range(1, n - 1):
    if p_list[i - 1] < p_list[i] < p_list[i + 1]:
        count += 1
    elif p_list[i - 1] > p_list[i] > p_list[i + 1]:
        count += 1

print(count)