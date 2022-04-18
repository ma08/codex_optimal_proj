

n, c = map(int, input().split())
fruits = list(map(int, input().split()))

# create a set of unique fruits
unique_fruits = set()

# iterate over the fruits
for fruit in fruits:
    # if the fruit is not in the set and we have enough capacity
    # add the fruit to the set
    if fruit not in unique_fruits and c - fruit >= 0:
        unique_fruits.add(fruit)
        c -= fruit

# print the number of unique fruits


# cook your dish here


N, M, K = map(int, input().split())


def check_validity(arr, n, m, k):
    for i in range(n):
        for j in range(m):
            if not (arr[i][j] == 1 or arr[i][j] == 0):
                return False
    if k > m * n:
        return False
    return True


def is_safe(i, j, arr, n, m, k):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return False
    if arr[i][j] == 0:
        return True
    return False


def get_count(arr, i, j, n, m, k):
    if k == 0:
        return 0
    count = 0
    if is_safe(i, j, arr, n, m, k):
        arr[i][j] = 1
        count = 1 + get_count(arr, i + 1, j, n, m, k - 1) + \
            get_count(arr, i - 1, j, n, m, k - 1) + \
            get_count(arr, i, j + 1, n, m, k - 1) + \
            get_count(arr, i, j - 1, n, m, k - 1)
        arr[i][j] = 0
    return count


def no_of_ways(arr, n, m, k):
    if not check_validity(arr, n, m, k):
        return 0
    count = 0
    for i in range(n):
        for j in range(m):
            count += get_count(arr, i, j, n, m, k)
    return count


arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
print(no_of_ways(arr, N, M, K))
print(len(unique_fruits))
