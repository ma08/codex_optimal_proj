
import sys

def main():

    n = int(sys.stdin.readline())
    skills = list(map(int, sys.stdin.readline().split()))[:n]
    pairs = [0]*n

    for i in range(n):
        pairs[i] = list(map(int, sys.stdin.readline().split()))[:n]

    mentors = [0]*(n+1)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and pairs[i-1][j-1] == 0 and skills[i-1] > skills[j-1]:
                mentors[i] += 1

    print(" ".join(map(str, mentors)))

if __name__ == '__main__':
    main()
