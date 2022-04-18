

# a, b, c = input().split(' ')
# print(len(set([a, b, c])))

a = [1, 2, 3]
b = [4, 5, 6]

c = zip(a, b)

for i, j in c:
    print(i, j)
