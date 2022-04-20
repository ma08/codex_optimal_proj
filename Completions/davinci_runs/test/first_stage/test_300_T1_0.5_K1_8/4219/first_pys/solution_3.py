

import sys

def is_honest(people, i, honest):
    if i in honest:
        return True
    if i not in people:
        return True
    for person in people[i]:
        if person[1] == 1 and person[0] not in honest:
            return False
    return True

def get_honest_count(people, N):
    honest = set()
    for i in range(1, N + 1):
        if is_honest(people, i, honest):
            honest.add(i)
    return len(honest)

def main():
    N = int(sys.stdin.readline().rstrip())
    people = {}
    for i in range(1, N + 1):
        A = int(sys.stdin.readline().rstrip())
        people[i] = []
        for j in range(A):
            x, y = map(int, sys.stdin.readline().rstrip().split())
            people[i].append((x, y))
    print(get_honest_count(people, N))

if __name__ == '__main__':
    main()