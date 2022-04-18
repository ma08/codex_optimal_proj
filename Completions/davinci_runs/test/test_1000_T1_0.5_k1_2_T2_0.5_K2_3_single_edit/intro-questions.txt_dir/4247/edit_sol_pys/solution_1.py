
n = int(input())


def is_sorted(p):
    for i in range(1, len(p)):
        if p[i - 1] > p[i]:
            return False
    return True

p = [int(x) for x in input().split()]

count = 0
for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1



def bubble_sort(p):
    count = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(p) - 1, 0, -1):
            if p[j] < p[j - 1]:
                p[j], p[j - 1] = p[j - 1], p[j]
                flag = True
                count += 1
    return count


print(bubble_sort(p))


def selection_sort(n, p):
    count = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if p[j] < p[minj]:
                minj = j
        if i != minj:
            p[i], p[minj] = p[minj], p[i]
            count += 1
    return count


print(selection_sort(n, p))
print(count)
