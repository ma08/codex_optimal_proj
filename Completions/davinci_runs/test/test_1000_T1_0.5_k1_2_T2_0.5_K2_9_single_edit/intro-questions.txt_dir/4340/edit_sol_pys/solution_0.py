from typing import List



def adjacent_replacements_algorithm(n: int, a: List[int]) -> List[int]:
    b = []
    for i in range(n):
        if a[i] % 2 == 0:
            b.append(a[i] - 1)
        else:
            b.append(a[i])
    return b


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*adjacent_replacements_algorithm(n, a))
