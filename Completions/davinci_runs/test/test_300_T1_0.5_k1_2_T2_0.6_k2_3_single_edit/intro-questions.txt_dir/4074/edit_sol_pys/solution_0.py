

# cook your dish here
def find(n, m):
    return n//m

test=int(input())
for i in range(test):
    n, m = map(int, input().split())
    print(find(n, m))
