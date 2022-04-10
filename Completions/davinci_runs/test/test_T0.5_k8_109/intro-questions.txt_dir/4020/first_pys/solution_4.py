

def midpoint(h1, m1, h2, m2):
	h = (h1 + h2) // 2
	m = (m1 + m2) // 2
	if (m1 + m2) % 2 == 1:
		if m == 60:
			h += 1
			m = 0
		else:
			m += 1
	return h, m

def main():
	h1, m1 = map(int, input().split(':'))
	h2, m2 = map(int, input().split(':'))
	h, m = midpoint(h1, m1, h2, m2)
	print('%02d:%02d' % (h, m))

if __name__ == '__main__':
	main()