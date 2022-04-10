

# Solution 1
import math

def solution(n):
    if n % 2 == 0:
        return 0
    else:
        i = 3
        while i <= math.sqrt(n) + 1:
            if n % i == 0:
                return 0
            i += 2
        return 1
# Solution 2
def solution(n):
    if n % 2 == 0:
        return 0
    else:
        i = 3
        while i <= math.sqrt(n) + 1:
            if n % i == 0:
                return 0
            i += 2
        return 1


# Test Cases

print(solution(11))
print(solution(14))
print(solution(61441))
print(solution(571576))
print(solution(2128506))
