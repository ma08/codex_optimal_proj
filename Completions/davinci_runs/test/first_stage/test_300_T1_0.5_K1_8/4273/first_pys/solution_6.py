

import sys
from collections import Counter

n = int(input())

names = []
for i in range(n):
    names.append(input())

#print(names)

# 文字列の先頭がM, A, R, C, Hのどれかかどうかを判定する関数
def is_start_with_march(s):
    if s[0] == 'M' or s[0] == 'A' or s[0] == 'R' or s[0] == 'C' or s[0] == 'H':
        return True
    else:
        return False

# 先頭文字がM, A, R, C, Hのどれかの文字列を抽出する
march_names = []
for name in names:
    if is_start_with_march(name):
        march_names.append(name)

#print(march_names)

# 先頭文字がM, A, R, C, Hのどれかの文字列のそれぞれの出現回数をカウントする
march_names_counter = Counter(march_names)
#print(march_names_counter)

# 出現回数が3以上のもののみを抽出する
march_names_counter_3_or_more = []
for key, value in march_names_counter.items():
    if value >= 3:
        march_names_counter_3_or_more.append(key)

#print(march_names_counter_3_or_more)

# 先頭文字がM, A, R, C, Hのどれかの文字列のそれぞれの出現回数が3以上のもののそれぞれについて、
# 先頭文字が同じものを抽出する
march_names_counter_3_or_more_same_start_letter = []
for name in march_names_counter_3_or_more:
    for name2 in march_names_counter_3_or_more:
        if name[0] == name2[0]:
            march_names_counter_3_or_more_same_start_letter.append(name2)

#print(march_names_counter_3_or_more_same_start_letter)

# 先頭文字がM, A, R, C, Hのどれかの文字列のそれぞれの出現回数が3以上のもののそれぞれについて、
# 先頭文字が同じものを抽出したものの出現回数をカウントする
march_names_counter_3_or_more_same_start_letter_counter = Counter(march_names_counter_3_or_more_same_start_letter)
#print(march_names_counter_3_or_more_same_start_letter_counter)

# 出現回数が3以上のもののそれぞれについて、
# 先頭文字が同じものを抽出したものの出現回数が3以上のもののそれぞれについて、
# それぞれの出現回数から3を引いた値を掛け合わせる
ans = 1
for key, value in march_names_counter_3_or_more_same_start_letter_counter.items():
    ans *= value - 2

print(ans)