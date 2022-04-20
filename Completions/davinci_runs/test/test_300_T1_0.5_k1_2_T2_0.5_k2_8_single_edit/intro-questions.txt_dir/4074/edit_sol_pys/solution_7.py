
# cook your dish here 
def find(n, k):
    if n % k == 0:
        return n // k
    return n // k + 1
test = int(input())
for i in range(test): 
    n, k = map(int, input().split())
    print(find(n, k))
