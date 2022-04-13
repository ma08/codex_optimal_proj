

# WORKS (TESTED)

N, C = [int(i) for i in input().split()]
seq = [int(i) for i in input().split()]  # sequence of numbers

freq_dict = {}  # dictionary of frequencies of numbers

for i in range(C+1):
    freq_dict[i] = 0

for i in seq:
    freq_dict[i] += 1

new_seq = []  # new sequence of numbers

for key in freq_dict:
    if freq_dict[key] != 0:
        new_seq.extend([key]*freq_dict[key])

print(" ".join([str(i) for i in new_seq]))
