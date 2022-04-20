

n = int(input())
a = list(map(int, input().split()))

def is_arithmetic_progression(a):
    return len(set(a[i+1] - a[i] for i in range(len(a) - 1))) == 1

if is_arithmetic_progression(a):
    print(0)
else:
    ans = n
    for i in range(n):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        if i + j + k + l + m == 0:
                            continue
                        b = a[:]
                        if j == 1:
                            b[i] += 1
                        else:
                            b[i] -= 1
                        if k == 1:
                            b[i+1] += 1
                        else:
                            b[i+1] -= 1
                        if l == 1:
                            b[i+2] += 1
                        else:
                            b[i+2] -= 1
                        if m == 1:
                            b[i+3] += 1
                        else:
                            b[i+3] -= 1
                        if is_arithmetic_progression(b):
                            ans = min(ans, j + k + l + m)
    if ans == n:
        print(-1)
    else:
        print(ans)