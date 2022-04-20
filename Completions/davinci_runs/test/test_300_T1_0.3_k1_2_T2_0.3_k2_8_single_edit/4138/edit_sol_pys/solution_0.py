
#!/bin/python3
# Solution

q = int(input())

for i in range(q):
    k = int(input())
    if k == 1:
        print(1)
    else:
        n = 1
        while k > n * (n + 1) // 2:
            n += 1
        k -= n * (n - 1) // 2
        print(str(n - k + 1)[-1])
