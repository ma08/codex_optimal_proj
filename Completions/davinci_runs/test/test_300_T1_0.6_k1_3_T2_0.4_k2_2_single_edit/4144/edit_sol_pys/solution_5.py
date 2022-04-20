
N = int(input())

# A[i] = the number of ways to make a sequence of length i that satisfies all
# conditions
# A[i] = A[i-1] + A[i-2]  # The last two elements are the same
# A[i] = A[i-2] + A[i-3] + \cdots + A[0]  # The last two elements are different
# A[i] = A[i-1] + A[i-1] - A[0]  # The last two elements are different
# A[i] = 2*A[i-1] - A[0]  # The last two elements are different

# A[0] = 1  # The empty sequence
# A[1] = 2  # The only way to make a sequence of length 1 is to have the same
# element twice
A = [0] * (N + 1)
A[0] = 1  # The empty sequence
A[1] = 2  # The only way to make a sequence of length 1 is to have the same
# element twice
for i in range(2, N + 1):
    A[i] = (2 * A[i - 1] - A[0]) % (10 ** 9 + 7)
print(A[N])  # The number of ways to make a sequence of length N
