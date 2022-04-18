

from collections import Counter

N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

cnt_dict = dict(Counter(S_list))

print("AC x {}".format(cnt_dict["AC"]) if "AC" in cnt_dict else "AC x 0")
print("WA x {}".format(cnt_dict["WA"]) if "WA" in cnt_dict else "WA x 0")
print("TLE x {}".format(cnt_dict["TLE"]) if "TLE" in cnt_dict else "TLE x 0")
print("RE x {}".format(cnt_dict["RE"]) if "RE" in cnt_dict else "RE x 0")
