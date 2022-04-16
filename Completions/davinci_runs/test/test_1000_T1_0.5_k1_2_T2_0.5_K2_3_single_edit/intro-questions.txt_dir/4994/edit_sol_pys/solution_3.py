

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        if i+j+k+l+m == n:
                            if (i*a + j*b + k*c + l*d + m*e) <= k:
                                cnt += 1
    print(cnt)

main()
