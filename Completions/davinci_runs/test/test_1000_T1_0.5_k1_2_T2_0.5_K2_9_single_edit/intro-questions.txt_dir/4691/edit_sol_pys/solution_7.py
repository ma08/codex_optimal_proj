

from collections import Counter

N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

cnt_dict = dict(Counter(S_list))

print("AC x {0}".format(cnt_dict["AC"]))
print("WA x {0}".format(cnt_dict["WA"]))
print("TLE x {0}".format(cnt_dict["TLE"]))
print("RE x {0}".format(cnt_dict["RE"]))
