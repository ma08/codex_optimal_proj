

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

if k == 1:
    print("YES")
    print("1 " * n)
    exit()

if k > n:
    print("NO")
    exit()

# if k > 1:
#     k = k - 1

# if k == 1:
#     print("YES")
#     print("1 " * n)
#     exit()

a_set = set(a)

if len(a_set) < k:
    print("NO")
    exit()

# print(a)
# print(a_set)

a_set = list(a_set)
a_set.sort()

# print(a_set)

a_set_dict = {}

for i in range(len(a_set)):
    a_set_dict[a_set[i]] = i % (k - 1) + 1

# print(a_set_dict)

# for i in range(len(a)):
#     a[i] = a_set_dict[a[i]]

# print(a)

print("YES")
for i in range(len(a)):
    print(a_set_dict[a[i]], end=" ")