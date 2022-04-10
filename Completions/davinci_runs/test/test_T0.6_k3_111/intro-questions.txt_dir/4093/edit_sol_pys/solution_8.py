
# SOLUTION
# For every test case, let's number the elements from 1 to N. Let the array be A. Now, let's find the minimum possible A[i] and the maximum possible A[i]. The minimum possible A[i] is M/N, where M is the sum of the array and N is the length of the array. The maximum possible A[i] is equal to the integer quotient of M/N plus 1. For example, if M=10 and N=5, then the minimum possible A[i] is 2 and the maximum possible A[i] is 3. Now, let's find the maximum possible value of A[i] - A[i-1]. It is equal to the difference between the maximum possible A[i] and the minimum possible A[i]. For example, if M=10 and N=5, then the maximum possible value of A[i] - A[i-1] is 1. We have to find the maximum possible sum of the absolute values of A[i] - A[i-1]. The maximum possible sum of the absolute values of A[i] - A[i-1] is equal to the multiplication of the length of the array and the maximum possible value of A[i] - A[i-1]. For example, if M=10 and N=5, then the maximum possible sum of the absolute values of A[i] - A[i-1] is 5

for _ in range(int(input())):
  n,m=map(int,input().split())
  print((m//n)*(n-1)+(m%n))
