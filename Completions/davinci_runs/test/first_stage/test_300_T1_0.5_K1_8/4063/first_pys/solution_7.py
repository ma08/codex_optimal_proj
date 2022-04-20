

# N is an even number, so the number of problems for ARCs must be N/2.
# We can use a counter to count the number of problems that have difficulty K or higher.
# The counter can be implemented using binary search.

# 関数定義
def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 入力
n = int(input())
d = list(map(int, input().split()))

# 二分探索
# d_i が d_k 以上である問題数をカウントする
# d_k より小さい問題数は n - counter である
counter = 0
for i in range(n):
    counter = binary_search(d, d[i])
    if counter == n // 2:
        print(1)
        exit()
    elif counter < n // 2:
        print(0)
        exit()

# 出力
print(0)