
def solution(n):
    x = 1
    if n == 1:
        return 1
    else:
        for i in range(n):
            if 2**i <= n and n < 2**(i + 1):
                x = i + 1
    return x
