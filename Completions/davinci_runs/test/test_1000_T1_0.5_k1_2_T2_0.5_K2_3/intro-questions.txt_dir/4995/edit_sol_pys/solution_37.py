

def read_input():
	n = int(input())
	m = []
	s = []
	for i in range(n):
		a, b = map(float, input().split())
		m.append(a)
		s.append(b)
	return n, m, s

def get_avg(n, m, s):
	summ = 0
	for i in range(n):
		summ += int(m[i] * 60 - s[i])
	if summ <= 0:
		return "measurement error"
	else:
		return summ / (n * 60)

def main():
	n, m, s = read_input()
	print(get_avg(n, m, s))

if __name__ == '__main__':
	main()
