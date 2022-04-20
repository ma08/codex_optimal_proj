# coding: utf-8

import sys

def main():
    N = int(sys.stdin.readline())
    people = [[] for _ in range(N)]
    for i in range(N):
        A_i = int(sys.stdin.readline())
        for j in range(A_i):
            x_ij, y_ij = map(int, sys.stdin.readline().split())
            people[i].append((x_ij-1, y_ij))
    print(N - solve(people))  # 全員が証言が一致するときは、嘘つきはいない

def solve(people):
    N = len(people)  # 人数
    for i in range(N):  # 人iについて
        for j in range(i+1, N):  # 人iと人jについて
            if is_consistent(people[i], people[j]):  # iとjの証言が一致しないとき
                return 2  # 嘘つきは2人いる
    return 1  # 嘘つきが1人以下のとき

def is_consistent(person1, person2):
    for x_i1, y_i1 in person1:
        for x_i2, y_i2 in person2:
            if x_i1 == x_i2 and y_i1 != y_i2:
                return True
    return False

if __name__ == '__main__':
    main()
