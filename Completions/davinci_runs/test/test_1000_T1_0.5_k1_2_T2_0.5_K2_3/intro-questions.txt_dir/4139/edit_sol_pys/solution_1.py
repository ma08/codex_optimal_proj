

import sys
import math

N = int(input())

# 入力値が10^9を超える場合、それ以上の数値は7,5,3のどれかの数字が含まれないため、処理を終了する
if N >= 1000000000:
    print(0)
    sys.exit()

# 入力値が10^8を超える場合、10^8までの7,5,3以外の数字が含まれる数を数える
if N >= 100000000:
    count = N - 100000000 + 1
    N = 100000000

# 入力値が10^7を超える場合、10^7までの7,5,3以外の数字が含まれる数を数える
if N >= 10000000:
    count = N - 10000000 + 1
    N = 10000000

# 入力値が10^6を超える場合、10^6までの7,5,3以外の数字が含まれる数を数える
if N >= 1000000:
    count = N - 1000000 + 1
    N = 1000000

# 入力値が10^5を超える場合、10^5までの7,5,3以外の数字が含まれる数を数える
if N >= 100000:
    count = N - 100000 + 1
    N = 100000

# 入力値が10^4を超える場合、10^4までの7,5,3以外の数字が含まれる数を数える
if N >= 10000:
    count = N - 10000 + 1
    N = 10000

# 入力値が10^3を超える場合、10^3までの7,5,3以外の数字が含まれる数を数える
if N >= 1000:
    count = N - 1000 + 1
    N = 1000

# 入力値が10^2を超える場合、10^2までの7,5,3以外の数字が含まれる数を数える
if N >= 100:
    count = N - 100 + 1
    N = 100

# 入力値が10^1を超える場合、10^1までの7,5,3以外の数字が含まれる数を数える
if N >= 10:
    count = N - 10 + 1
    N = 10

# 入力値が10^0を超える場合、10^0までの7,5,3以外の数字が含まれる数を数える
if N >= 1:
    count = N - 1 + 1
    N = 1

# 入力値が10^8より小さい場合、7,5,3以外の数字が含まれないため、処理を終了する
if N == 0:
    print(count)
    sys.exit()

# 入力値が10^7より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 1:
    count = count + 10
    N = 0

# 入力値が10^6より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 10:
    count = count + 90
    N = 0

# 入力値が10^5より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 100:
    count = count + 900
    N = 0

# 入力値が10^4より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 1000:
    count = count + 9000
    N = 0

# 入力値が10^3より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 10000:
    count = count + 90000
    N = 0

# 入力値が10^2より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 100000:
    count = count + 900000
    N = 0

# 入力値が10^1より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 1000000:
    count = count + 9000000
    N = 0

# 入力値が10^0より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 10000000:
    count = count + 90000000
    N = 0

# 入力値が10^-1より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 100000000:
    count = count + 900000000
    N = 0

# 入力値が10^-2より小さい場合、7,5,3以外の数字が含まれる数を数える
if N == 1000000000:
    count = count + 9000000000
    N = 0

print(count)
