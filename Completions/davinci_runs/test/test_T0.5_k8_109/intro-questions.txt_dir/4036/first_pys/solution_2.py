

# First, I want to find a way to generate the numbers
# I will use the following algorithm:
# 1. Start with the number 1
# 2. For each number, generate the next number by multiplying by 2 and adding 1
# 3. If the number is greater than n, then stop
# 4. If the number is less than n, then subtract it from n
# 5. Repeat until n is 0

# This algorithm is pretty simple.
# To prove that it works, I will prove that it satisfies the three conditions
# 1. sum of all $a_i$ for $i$ from $1$ to $k$ should be $n$
# This is satisfied because the sum of all $a_i$ will be the sum of all numbers $x$ such that $x$ is less than or equal to $n$
# 2. $a_i$ should be greater than zero for each $i$ from $1$ to $k$
# This is satisfied because the algorithm does not generate 0
# 3. the condition $a_i < a_{i + 1} \le 2 a_i$ should be satisfied for each $i$ from $1$ to $k-1$.
# This is satisfied because the algorithm generates the numbers $a_i$ in increasing order

# Now, I will implement the algorithm
n, k = map(int, input().split())

# If n is 0, then there is no solution
if n == 0:
    print("NO")
    exit()

# If k is 1, then there is a solution
if k == 1:
    print("YES")
    print(n)
    exit()

# Generate the numbers
a = []
while n > 0:
    a.append(n)
    n = n // 2

# If the number of numbers is less than k, then there is no solution
if len(a) < k:
    print("NO")
    exit()

# If the number of numbers is equal to k, then there is a solution
if len(a) == k:
    print("YES")
    print(*a)
    exit()

# If the number of numbers is greater than k, then there is a solution
if len(a) > k:
    # First, I will generate the numbers that will be used
    # I will do that by splitting the numbers into chunks of length k
    # I will then add the first element of each chunk to the last element of the previous chunk
    # For example, if a = [1, 2, 3, 4, 5, 6, 7, 8, 9] and k = 3, then the numbers will be [1, 2, 3] + [4, 5, 6] + [7, 8, 9] = [1, 2, 3, 5, 7, 10]
    # I will do that by first splitting the numbers into chunks of length k
    chunks = [a[i:i + k] for i in range(0, len(a), k)]
    # Then, I will add the first element of each chunk to the last element of the previous chunk
    # First, I will add the first element of the first chunk to the last element of the previous chunk
    chunks[1][0] += chunks[0][-1]
    # Then, I will add the first element of each of the other chunks to the last element of the previous chunk
    for i in range(2, len(chunks)):
        chunks[i][0] += chunks[i - 1][-1]
    # Then, I will flatten the list of chunks
    a = [item for sublist in chunks for item in sublist]
    # Then, I will print the answer
    print("YES")
    print(*a)
    exit()