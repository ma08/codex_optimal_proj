
import sys

def main():
    n = int(sys.stdin.readline())
    people = [[] for _ in range(n)]
    for i in range(n):
        a_i = int(sys.stdin.readline())
        for j in range(a_i):
            x_ij, y_ij = map(int, sys.stdin.readline().split())  # x_ij: 友達の順番, y_ij: 友達の真偽
            people[i].append((x_ij - 1, y_ij))
    print(n - solve(people))

def solve(people):
    n = len(people)
    for i in range(n):
        for j in range(i + 1, n):
            if is_consistent(people[i], people[j]):
                return 2
    return 1

def is_consistent(person1, person2):
    for x_i1, y_i1 in person1:
        for x_i2, y_i2 in person2:
            if x_i1 == x_i2 and y_i1 != y_i2:
                return True
    return False

if __name__ == '__main__':
    main()
