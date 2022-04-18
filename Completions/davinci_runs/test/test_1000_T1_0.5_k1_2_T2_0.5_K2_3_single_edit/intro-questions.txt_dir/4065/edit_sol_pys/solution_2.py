from typing import List



def solve(n: int, a: List[int]) -> int:
    contests = []

    for i in range(n):
        for j in range(i+1, n):
            if a[j] > a[i] * 2:
                break
            contests.append((a[i], a[j]))

    contests.sort()

    max_len = 0
    max_contest = None

    for i in range(len(contests)):
        this_contest = [contests[i]]
        for j in range(i+1, len(contests)):
            if contests[j][0] > this_contest[-1][1] * 2:
                break
            this_contest.append(contests[j])
        if len(this_contest) > max_len:
            max_len = len(this_contest)
            max_contest = this_contest

    return max_len


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    res = solve(n, a)
    print(res)


if __name__ == '__main__':
    main()
