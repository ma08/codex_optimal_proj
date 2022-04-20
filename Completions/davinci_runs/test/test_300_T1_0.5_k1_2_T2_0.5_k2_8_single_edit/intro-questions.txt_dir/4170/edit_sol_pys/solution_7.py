import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy


N = int(input()) # 数値
A = [int(input()) for i in range(N)] # リスト
A = list(map(int, input().split())) # リスト（スペース区切り）
A = [list(map(int, input().split())) for i in range(N)] # リストのリスト（スペース区切り）
S = input() # 文字列

# 再帰関数
def rec(i):
    if i == N:
        print(A)
        return
    for j in range(N):
        A[i] = j
        rec(i + 1)

# スタック
stack = []
stack.append(1)
stack.append(2)
stack.pop()

# キュー
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

# 文字列
S = "abc"
S[0] # 文字列の0番目の文字
S[-1] # 文字列の最後の文字
S[1:3] # 文字列の1番目から3番目の文字まで
S[::-1] # 文字列を逆にする

# 文字列の検索
S.find("a") # 文字列Sから文字列aが最初に出てくる位置を返す
S.rfind("a") # 文字列Sから文字列aが最後に出てくる位置を返す
S.count("a") # 文字列Sに文字列aがいくつあるかを返す

# 文字列の置換
S.replace("a", "b") # 文字列Sの中の文字列aをbに置換する

# 文字列の分割
S.split("a") # 文字列Sを文字列aで分割してリストを返す

# 文字列の結合
"".join(["a", "b", "c"]) # リスト["a", "b", "c"]を空文字列で結合する

# 文字列の判定
S.isalnum() # 文字列Sが英数字かどうか
S.isalpha() # 文字列Sが英字かどうか
S.isdigit() # 文字列Sが数字かどうか
S.islower() # 文字列Sが小文字かどうか
S.isupper() # 文字列Sが大文字かどうか
S.isspace() # 文字列Sが空白かどうか
S.istitle() # 文字列Sがタイトルケースかどうか

# 文字列の変換
S.lower() # 文字列Sを小文字に変換する
S.upper() # 文字列Sを大文字に変換する
S.title() # 文字列Sをタイトルケースに変換する

# 文字列のトリミング
S.lstrip() # 文字列Sの左端の空白を削除する
S.rstrip() # 文字列Sの右端の空白を削除する
S.strip() # 文字列Sの左右端の空白を削除する

# 文字列の出力
print("%.2f" % 1.2345) # 文字列1.2345を小数点第2位まで表示する
print("{} {}".format(1, 2)) # 文字列1 2を出力する
print("{0} {1}".format(1, 2)) # 文字列1 2を出力する
print("{1} {0}".format(1, 2)) # 文字列2 1を出力する

# 数値
a = 1
a += 1 # a = a + 1と同じ
a -= 1 # a = a - 1と同じ
a *= 2 # a = a * 2と同じ
a /= 2 # a = a / 2と同じ
a //= 2 # a = a // 2と同じ
a %= 2 # a = a % 2と同じ
a **= 2 # a = a ** 2と同じ

# 累積和
A = [1, 2, 3, 4, 5]
B = [0]
B.extend(accumulate(A))

# ソート
A = [1, 3, 2, 4, 5]
A.sort() # A = [1, 2, 3, 4, 5]
A.sort(reverse=True) # A = [5, 4, 3, 2, 1]
sorted(A) # [1, 2, 3, 4, 5]
sorted(A, reverse=True) # [5, 4, 3, 2, 1]

# 二分探索
def binary_search(A, x):
    l = -1
    r = len(A)
    while r - l > 1:
        mid = (l + r) // 2
        if A[mid] >= x:
            r = mid
        else:
            l = mid
    return r

# 順列
for p in permutations(A):
    print(p)

# 組み合わせ
for c in combinations(A, 3):
    print(c)

# 組み合わせ（重複あり）
for c in combinations_with_replacement(A, 3):
    print(c)

# 素数
def is_prime(
