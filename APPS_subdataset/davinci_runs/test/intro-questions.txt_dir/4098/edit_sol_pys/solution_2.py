

from collections import defaultdict
from heapq import heappush, heappop, heapify
from typing import List, Tuple, Dict, Set

from sys import stdin, stdout

def read_ints():
    return list(map(int, stdin.readline().split()))


def read_int():

    return int(stdin.readline())

def read_lines(n: int):
    return [stdin.readline().strip() for _ in range(n)]


def write_line(s: str):
    stdout.write(s)
    stdout.write("\n")


def write_lines(lines: List[str]):
    stdout.write("\n".join(lines))
    stdout.write("\n")


def solve(n: int, k: int, skills: List[int]):
    # return number of students that can be included in k teams 
    # such that the difference between the skills of any 2 students
    # in a team is no more than 5
    d = defaultdict(lambda: 0)
    for skill in skills:
        d[skill] += 1
    heap = []
    for skill, count in d.items():
        heappush(heap, (count, skill))
    ans = 0
    while heap:
        count, skill = heappop(heap)
        if count <= k:
            ans += count
            k -= count
            if k == 0:
                return ans
        else:
            ans += k
            return ans
        if k == 0:
            return ans
        for i in range(skill-5, skill+1):
            if i in d:
                heappush(heap, (d[i], i))
    return ans


def main():
    n, k = read_ints()
    skills = read_ints()
    ans = solve(n, k, skills)
    write_line(str(ans))


if __name__ == "__main__":
    main()
