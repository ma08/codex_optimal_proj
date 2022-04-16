import sys

diff_table = [v]
while len(diff_table[-1]) > 1:
    diff_table.append([])
    for i in range(len(diff_table[-2]) - 1):
        diff_table[-1].append(diff_table[-2][i + 1] - diff_table[-2][i])
for i in range(len(diff_table)):
    print("\t".join(map(str, diff_table[i])))
print()
