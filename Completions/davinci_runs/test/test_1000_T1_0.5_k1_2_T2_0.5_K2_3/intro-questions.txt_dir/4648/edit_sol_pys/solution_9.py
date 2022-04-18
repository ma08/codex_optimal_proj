
t = int(input())
for _ in range(t):
    n = int(input())
    if n==1 or n==0:
        print(n)
    else:
        count = 0
        while n>0:
            if n%6==0:
                n //= 6
            elif n%3==0:
                n *= 2
                n //= 3
            else:
                count = -1
                break
            count += 1
        print(count)
