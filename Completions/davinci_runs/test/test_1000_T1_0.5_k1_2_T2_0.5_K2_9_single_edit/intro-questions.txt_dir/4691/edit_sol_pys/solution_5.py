
from collections import Counter

N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

cnt_dict = dict(Counter(S_list))
for key in cnt_dict.keys():
    print("{} x {}".format(key, cnt_dict[key]))
