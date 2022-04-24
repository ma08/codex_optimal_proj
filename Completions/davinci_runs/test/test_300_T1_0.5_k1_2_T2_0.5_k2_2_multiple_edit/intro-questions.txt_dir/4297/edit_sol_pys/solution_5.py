def solve(n):
    num = n
    while True:
        if num % 2 == 0:
            break
        num += n
    print(num)
 
 
n = int(input())
solve(n)
