
# cook your dish here
def find(n, k):
    return (n // k) + 1
 
 
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(find(n, k))
