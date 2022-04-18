
def solve(n, s):
    if n % 2 == 1:
        return -1
    else:
        s = list(s)
        for i in range(n//2):
            j = n-i-1
            if s[i] != s[j]:
                return -1
        return n//2
    
for _ in range(int(input())): 
    n = int(input())
    s = input().strip()
    print(solve(n, s))
