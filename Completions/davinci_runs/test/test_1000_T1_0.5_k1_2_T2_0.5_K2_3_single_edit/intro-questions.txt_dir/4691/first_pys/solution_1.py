

from collections import Counter

N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

cnt_dict = dict(Counter(S_list))

print("AC x {}".format(cnt_dict["AC"]))
print("WA x {}".format(cnt_dict["WA"]))
print("TLE x {}".format(cnt_dict["TLE"]))
print("RE x {}".format(cnt_dict["RE"]))