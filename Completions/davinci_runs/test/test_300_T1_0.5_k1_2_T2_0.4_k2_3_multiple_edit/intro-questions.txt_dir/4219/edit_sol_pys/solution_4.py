

import sys

def main():
    # read input
    n = int(sys.stdin.readline())
    testimonies = []
    for i in range(n):
        a = int(sys.stdin.readline())
        testimonies.append([])
        for j in range(a):
            testimonies[i].append([int(x) for x in sys.stdin.readline().split()])

    # find max dishonest people
    max_dishonest_people = 0
    for i in range(2**n):
        # check if it is possible to have i dishonest people
        dishonest_people = 0
        for j in range(n):
            if (i & (1 << j)) == 0:
                continue
            dishonest_people += 1
            for testimony in testimonies[j]:
                if (i & (1 << (testimony[0] - 1))) != 0 and testimony[1] == 0:
                    dishonest_people = -1
                    break
            if dishonest_people == -1:
                break
        if dishonest_people == -1:
            continue
        max_dishonest_people = max(max_dishonest_people, dishonest_people)

    print(max_dishonest_people)

if __name__ == '__main__':
    main()
