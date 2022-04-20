

# Solution
n = int(input())
a = [[0, 0] for i in range(n)]
for i in range(n):
    a[i][0], a[i][1] = map(int, input().split())

# a[i] = [a[i][0], a[i][1]]

# print(a)

def check(a):
    for i in range(n):
        if a[i][0] == a[i][1] or a[i][0] == a[a[i][0]][0] or a[i][0] == a[a[i][0]][1]:
            return False
    return True

def get_next(a, i):
    for j in range(n):
        if a[j][0] == i or a[j][1] == i:
            return j
    return -1

def get_next_next(a, i):
    for j in range(n):
        if a[j][0] == i or a[j][1] == i:
            return a[j][0] if a[j][1] == i else a[j][1]
    return -1

def get_next_next_next(a, i):
    for j in range(n):
        if a[j][0] == i or a[j][1] == i:
            return get_next(a, a[j][0] if a[j][1] == i else a[j][1])
    return -1

def get_next_next_next_next(a, i):
    for j in range(n):
        if a[j][0] == i or a[j][1] == i:
            return get_next_next(a, a[j][0] if a[j][1] == i else a[j][1])
    return -1


def get_order(a):
    order = [-1] * n
    order[0] = 1
    order[1] = get_next(a, order[0])
    order[2] = get_next_next(a, order[0])
    order[3] = get_next_next_next(a, order[0])
    order[4] = get_next_next_next_next(a, order[0])
    # print(order)
    for i in range(n):
        if order[i] == -1:
            order[i] = get_next(order, i)
    return order

# print(check(a))

# print(get_order(a))

def get_order_2(a):
    order = [-1] * n
    order[0] = get_next(a, a[0][0])
    order[1] = a[order[0]][0] if a[order[0]][1] == a[0][0] else a[order[0]][1]
    order[2] = get_next(a, order[0])
    order[3] = get_next_next(a, order[0])
    order[4] = get_next_next_next(a, order[0])
    # print(order)
    for i in range(n):
        if order[i] == -1:
            order[i] = get_next(order, i)
    return order

print(get_order_2(a))

# def get_order_3(a):
#     order = [-1] * n
#     order[0] = get_next(a, a[0][0])
#     order[1] = get_next(a, a[0][1])
#     order[2] = get_next_next(a, a[0][0])
#     order[3] = get_next_next_next(a, a[0][0])
#     order[4] = get_next_next_next_next(a, a[0][0])
#     # print(order)
#     for i in range(n):
#         if order[i] == -1:
#             order[i] = get_next(order, i)
#     return order

# print(get_order_3(a))