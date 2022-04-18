
import sys

def solve(n: int) -> int:
    if n <= 1:
        return -1
    elif n % 25 == 0:
        return 0
    else:
        digits = [int(d) for d in str(n)]
        idx = 0
        while digits[idx] == 0:
            idx += 1
        digits[idx] = (digits[idx] - 1) % 10
        if digits[idx] == 0:
            return -1
        else:
            return 1 + solve(int(''.join([str(d) for d in digits])))

# main
n: int = int(sys.stdin.readline().strip())
print(solve(n))
