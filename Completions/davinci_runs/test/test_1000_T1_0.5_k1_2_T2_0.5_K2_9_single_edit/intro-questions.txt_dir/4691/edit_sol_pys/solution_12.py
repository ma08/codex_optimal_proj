

from collections import Counter

N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

cnt_dict = dict(Counter(S_list))

print("AC x {}".format(cnt_dict.get("AC", 0)))
print("WA x {}".format(cnt_dict.get("WA", 0)))
print("TLE x {}".format(cnt_dict.get("TLE", 0)))
print("RE x {}".format(cnt_dict.get("RE", 0)))
