
# SOLUTION
# For every test case, let's number the elements from 1 to N. Let the array be A.
# Now, let's find the minimum possible A[i] and the maximum possible A[i].
# The minimum possible A[i] is M/N, where M is the sum of the array and N is the length of the array.
# The maximum possible A[i] is equal to the integer quotient of M/N plus 1.
# For example, if M=10 and N=5, then the minimum possible A[i] is 2 and the maximum possible A[i] is 3.
# Now, let's find the maximum possible value of A[i] - A[i-1].
# It is equal to the difference between the maximum possible A[i] and the minimum possible A[i].
# For example, if M=10 and N=5, then the maximum possible value of A[i] - A[i-1] is 1.
# We have to find the maximum possible sum of the absolute values of A[i] - A[i-1].
# The maximum possible sum of the absolute values of A[i] - A[i-1] is equal to the multiplication of the length of the array and the maximum possible value of A[i] - A[i-1].
# For example, if M=10 and N=5, then the maximum possible sum of the absolute values of A[i] - A[i-1] is 5.
# Let's prove this.
# Consider two numbers X and Y.
# If X < Y, then |X - Y| = Y - X.
# If X > Y, then |X - Y| = X - Y.
# If we take the sum of the absolute values of X - Y, we will obtain |X - Y| + |Y - X| = |X - Y| + |X - Y| = 2|X - Y|.
# So, if we take the sum of the absolute values of A[i] - A[i-1], we will obtain 2*|A[i] - A[i-1]|, which is equal to 2*(A[i] - A[i-1]), which is equal to A[i] - A[i-1] + A[i-1] - A[i], which is equal to A[i] - A[i-2] + A[i-1] - A[i], which is equal to A[i] - A[i-2].
# So, the sum of the absolute values of A[i] - A[i-1] is equal to A[i] - A[i-2].
# If A[i] - A[i-2] = A[i] - A[i-1] + A[i-1] - A[i-2], then A[i] - A[i-2] = A[i] - A[i-1] + A[i-1] - A[i-2], which is equal to A[i] - A[i-1] + A[i-1] - A[i-2].
# So, the sum of the absolute values of A[i] - A[i-1] is equal to A[1] - A[0] + A[2] - A[1] + A[3] - A[2] + ... + A[N-1] - A[N-2] + A[N] - A[N-1].
# The maximum possible value of A[i] - A[i-1] is equal to the difference between the maximum possible A[i] and the minimum possible A[i].
# The maximum possible sum of the absolute values of A[i] - A[i-1] is equal to the multiplication of the length of the array and the maximum possible value of A[i] - A[i-1].
# For example, if M=10 and N=5, then the maximum possible sum of the absolute values of A[i] - A[i-1] is 5.

for _ in range(int(input())):
  n,m=map(int,input().split())
  print((m//n)*(n-1)+(m%n))