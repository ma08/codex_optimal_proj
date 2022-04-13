# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum([a[i]*b[i] for i in range(n)]))
