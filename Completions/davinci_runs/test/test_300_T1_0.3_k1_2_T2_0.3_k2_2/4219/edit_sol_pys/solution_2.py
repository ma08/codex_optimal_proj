
import sys

def main():
    N = int(sys.stdin.readline())
    people = [[] for _ in range(N)]  # people[i] = [(x_ij, y_ij) for j in range(A_i)]
    for i in range(N):
        A_i = int(sys.stdin.readline())
        for j in range(A_i):
            x_ij, y_ij = map(int, sys.stdin.readline().split())
            people[i].append((x_ij - 1, y_ij))
    print(N - solve(people))

def solve(people):
    N = len(people)
    for i in range(N):
        for j in range(i + 1, N):
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
