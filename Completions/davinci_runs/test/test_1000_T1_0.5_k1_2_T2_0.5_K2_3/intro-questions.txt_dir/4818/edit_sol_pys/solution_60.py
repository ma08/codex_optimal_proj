

import sys


def main():
	n, m = map(int, input().split())
	tasks = list(map(int, input().split()))
	intervals = list(map(int, input().split()))
	tasks.sort()
	intervals.sort()

	best = 0
	tasks_index = 0
	intervals_index = 0
	while tasks_index < n and intervals_index < m:
		if tasks[tasks_index] <= intervals[intervals_index]:
			best += 1
			tasks_index += 1
		intervals_index += 1
	print(best)


if __name__ == '__main__':
	main()
