

"""
Solution outline
	- Let X and Y be the number of books liked by Alice and Bob respectively.
	- We need to find a set of books with X >= k, Y >= k and sum(t_i) is minimized.
	  This means, we need to find a set of books with X >= k and sum(t_i) is minimized.
	  Then, we find a set of books with Y >= k and sum(t_i) is minimized.
	- For the first set, we can keep track of the number of books like by Alice in a sliding window of size k.
	  We can keep track of the sum of t_i in the window as well, and keep track of the minimum sum seen so far.
	  This can be done in linear time.
	- For the second set, we can keep track of the number of books like by Bob in a sliding window of size k.
	  We can keep track of the sum of t_i in the window as well, and keep track of the minimum sum seen so far.
	  This can be done in linear time.
	- We return the minimum of the two sums.
"""
def min_books_to_read(t, a, b, k):
	# Find minimum sum of t_i, such that sum(a_i) >= k
	min_sum = sum(t[:k])
	a_sum = sum(a[:k])
	if a_sum < k:
		return -1

	for i in xrange(k, len(t)):
		a_sum += a[i] - a[i-k]
		if a_sum < k:
			break

		min_sum = min(min_sum, sum(t[i-k+1:i+1]))

	# Find minimum sum of t_i, such that sum(b_i) >= k
	min_sum2 = sum(t[:k])
	b_sum = sum(b[:k])
	if b_sum < k:
		return -1

	for i in xrange(k, len(t)):
		b_sum += b[i] - b[i-k]
		if b_sum < k:
			break

		min_sum2 = min(min_sum2, sum(t[i-k+1:i+1]))

	return min(min_sum, min_sum2)

if __name__ == '__main__':
	n,k = map(int, raw_input().strip().split())
	t = []
	a = []
	b = []
	for i in xrange(n):
		t_i, a_i, b_i = map(int, raw_input().strip().split())
		t.append(t_i)
		a.append(a_i)
		b.append(b_i)

	print min_books_to_read(t, a, b, k)