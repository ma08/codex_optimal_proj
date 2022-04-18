
from collections import defaultdict

N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

cnt_dict = defaultdict(int)
for s in S_list:
    cnt_dict[s] += 1

print("AC x {}".format(cnt_dict["AC"]))
print("WA x {}".format(cnt_dict["WA"]))
print("TLE x {}".format(cnt_dict["TLE"]))
print("RE x {}".format(cnt_dict["RE"]))
