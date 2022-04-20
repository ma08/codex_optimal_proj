

#Solution

# cook your dish here
cases = int(input())
for i in range(cases):
    n, a, b = map(int, input().split())
    if a > b:
        b, a = a, b
    if n == 1:
        print(a)
    elif n == 2:
        print(a*2)
    else:
        print(a + (n//2)*b + (n%2)*a)