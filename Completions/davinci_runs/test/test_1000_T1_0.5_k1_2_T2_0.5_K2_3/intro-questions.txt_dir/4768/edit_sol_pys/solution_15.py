def main():
    n, k = map(int, input().split())
    dna = []
    for i in range(n):
        dna.append(input())

    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main2():

    n, k = map(int, input().split())
    dna = []
    for i in range(n):
        dna.append(input())
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main3():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main4():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main5():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main6():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main7():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main8():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main9():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


def main10():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


if __name__ == '__main__':
    main()
