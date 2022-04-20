

from typing import List
import sys

def solve(n: int) -> int:
    if n <= 1:
        return -1
    elif n % 25 == 0: # 25 = 5^2
        return 0
    else:
        digits: List[int] = [int(d) for d in str(n)]
        idx: int = 0
        while digits[idx] == 0:
            idx += 1
        digits[idx] = (digits[idx] - 1) % 10
        if digits[idx] == 0:
            return -1
        else:
            return 1 + solve(int(''.join([str(d) for d in digits])))

# main
n: int = int(sys.stdin.readline().strip()) # type: ignore
print(solve(n))
