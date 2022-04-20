

# output the number of codes that correctly solve this problem

# input
n, m, c = map(int, input().split())
b_list = list(map(int, input().split()))
a_list = []
for i in range(n):
    a_list.append(list(map(int, input().split())))

# calc
count = 0
for a in a_list:
    if sum([a[i]*b_list[i] for i in range(m)]) + c > 0:
        count += 1

# output
print(count)