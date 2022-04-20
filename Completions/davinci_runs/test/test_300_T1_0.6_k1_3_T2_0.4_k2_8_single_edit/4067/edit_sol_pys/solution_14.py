from collections import Counter


def main():
	n = int(input())
	s = input()
	d = Counter(s)
	print(d)
	if d['1'] < d['2']: d['1'] += 1; d['2'] -= 1
	elif d['1'] > d['2']: d['1'] -= 1; d['2'] += 1
	print('0' * d['0'] + '1' * d['1'] + '2' * d['2'], end='')

if __name__ == '__main__':
	main()
