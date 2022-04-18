

import sys

def main():
    # Read input
    n = int(sys.stdin.readline())
    testimonies = []
    for i in range(n):
        a = int(sys.stdin.readline())
        testimonies.append([])
        for j in range(a):
            testimonies[i].append([int(x) for x in sys.stdin.readline().split()])

    # Find max honest people
    max_honest_people = 0
    for i in range(2**n):
        # Check if it is possible to have i honest people
        honest_people = 0
        for j in range(n):
            if (i & (1 << j)) == 0: # j-th person is not honest
                continue
            honest_people += 1
            for testimony in testimonies[j]:
                if (i & (1 << (testimony[0] - 1))) != 0 and testimony[1] == 0: # j-th person lied
                    honest_people = -1
                    break
            if honest_people == -1:
                break
        if honest_people == -1:
            continue
        max_honest_people = max(max_honest_people, honest_people)

    print(max_honest_people)

if __name__ == '__main__':
    main()
