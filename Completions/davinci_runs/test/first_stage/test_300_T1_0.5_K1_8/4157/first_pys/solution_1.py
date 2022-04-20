

import sys

def find_seq(n, seq):
	seq_dict = {}
	for i in range(n):
		seq_dict[seq[i]] = i

	seq.sort()

	for i in range(n-1):
		if seq[i] * 3 == seq[i+1]:
			continue
		if seq[i] * 2 == seq[i+1]:
			continue
		return False

	result = [0] * n
	for i in range(n):
		result[seq_dict[seq[i]]] = seq[i]
	return result


if __name__ == "__main__":
	n = int(sys.stdin.readline().strip())
	seq = [int(i) for i in sys.stdin.readline().strip().split()]
	result = find_seq(n, seq)
	for i in result:
		print(i, end=" ")
	print()