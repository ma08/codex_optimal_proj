

import itertools

n, m = map(int, input().split())
q = [list(map(int, input().split())) for i in range(m)]

possible_numbers = [str(i) for i in range(10)]

for i in range(m):
    s_i, c_i = q[i][0] - 1, str(q[i][1])
    # possible_numbers[s_i]には、s_i番目の桁に入る可能性のある数字が入っている
    # ここでは、c_iをs_i番目の桁に入る可能性のある数字に追加し、
    # それ以外の数字を削除する
    possible_numbers[s_i] = c_i
    for j in range(10):
        if str(j) != c_i:
            possible_numbers[s_i] = possible_numbers[s_i].replace(str(j), '')

# 全ての桁について、c_iが入る可能性のある数字を決めたので、
# それらを組み合わせて、n桁の数字を作る
# itertools.product(*possible_numbers)は、
# possible_numbersの要素をそれぞれ取り出し、それらを組み合わせて、
# 全ての組み合わせを列挙する
ans = -1
for i in itertools.product(*possible_numbers):
    i = int(''.join(i))
    if len(str(i)) == n and i >= 0:
        if ans == -1:
            ans = i
        else:
            ans = min(ans, i)
print(ans)

# Reference code
n, m = map(int, input().split())
q = [list(map(int, input().split())) for i in range(m)]

ans = -1
for i in range(1000, 10000):
    s = str(i)
    ok = True
    for j in range(m):
        if s[q[j][0]-1] != str(q[j][1]):
            ok = False
    if ok:
        ans = i
        break
print(ans)
