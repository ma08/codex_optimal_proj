# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

print(len(M.union(N)))

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

print(len(M.intersection(N)))

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

print(len(M.difference(N)))

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

print(len(M.symmetric_difference(N)))

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

print(M.issubset(N))

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

print(M.issuperset(N))

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

print(M.isdisjoint(N))

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

for i in sorted(M.union(N)):
    print(i)

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

for i in sorted(M.intersection(N)):
    print(i)

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

for i in sorted(M.difference(N)):
    print(i)

# Enter your code here. Read input from STDIN. Print output to STDOUT

m, M = input(), set(map(int, input().split()))
n, N = input(), set(map(int, input().split()))

for i in sorted(M.symmetric_difference(N)):
    print(i)
