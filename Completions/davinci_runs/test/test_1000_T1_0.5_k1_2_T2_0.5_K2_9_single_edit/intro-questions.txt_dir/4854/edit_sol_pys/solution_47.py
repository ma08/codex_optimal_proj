
#
# WORKS

[n, c] = [int(i) for i in input().split()]
seq = [int(i) for i in input().split()]

freq_dict = {}

for i in range(c+1):
    freq_dict[i] = 0

for i in seq:
    freq_dict[i] += 1

new_seq = []

for key in freq_dict:
    if freq_dict[key] != 0:
        new_seq.extend([key]*freq_dict[key])

print(" ".join([str(i) for i in new_seq]))
