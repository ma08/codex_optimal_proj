

def solution(n):
    """
    >>> solution(11)
    2
    >>> solution(14)
    0
    >>> solution(61441)
    2
    >>> solution(571576)
    10
    >>> solution(2128506)
    3
    """
    answer = 0
    for i in range(1, n+1):
        if (i%2 == 0) and (n%i == 0):
            answer += 1
    return answer