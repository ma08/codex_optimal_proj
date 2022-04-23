

def solve(query, solution):
	if query == 1:
		solution.append('1')
	elif query == 2:
		solution.append('2')
	else:
		# 1 + 2 + 3 + 4 + ... + n
		n = 1
		while n*(n+1) < query*2:
			n += 1
		n -= 1
		# I need to find the digit at the position query-n in the block from 1 to n
		# So I find the position of query-n in the sequence
		pos = 0
		for i in range(1, n+1):
			pos += i*(i+1)
		pos = query - pos
		
		# I find the number at this position
		num = 0
		while pos != 0:
			num += 1
			if pos > num:
				pos -= num
			else:
				break
		# And finally I find the digit
		solution.append(str(num)[pos-1:pos])
		
	return solution
	
def main():
	q = int(input())
	queries = [int(input()) for _ in range(q)]
	solution = []
	for query in queries:
		solve(query, solution)
	print('\n'.join(solution))
	
main()
