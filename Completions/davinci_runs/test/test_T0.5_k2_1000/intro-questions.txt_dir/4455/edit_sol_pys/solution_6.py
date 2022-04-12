

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    skills = list(map(int, sys.stdin.readline().split()))
    pairs = [0]*k

    for i in range(k):
        pairs[i] = list(map(int, sys.stdin.readline().split()))

    mentors = [0]*n

    for i in range(k):
        if skills[pairs[i][0]-1] > skills[pairs[i][1]-1]:
            mentors[pairs[i][0]-1] += 1
        else:
            mentors[pairs[i][1]-1] += 1

    print(" ".join(map(str, mentors)))

if __name__ == '__main__':
    main()
