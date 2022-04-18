

from collections import defaultdict


def find_ladica(ladice, i):
    if ladice[i[0]] == 0:
        return i[0]
    elif ladice[i[1]] == 0:
        return i[1]
    else:
        return 0


def find_possible_ladica(ladice, i):
    for k in range(len(ladice)):
        if ladice[k] == 0:
            continue
        if ladice[k] == i[0]:
            return k
        elif ladice[k] == i[1]:
            return k
        else:
            continue
    return 0


def find_ladica_from_ladica(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            a = ladice[a]
            b = ladice[b]
            if a == b:
                return 0
            continue


def find_ladica_from_ladica2(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[a] == i[0]:
                return a
            elif ladice[b] == i[1]:
                return b
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica3(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == 0:
                return ladice[a]
            elif ladice[ladice[b]] == 0:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica4(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == a:
                return ladice[a]
            elif ladice[ladice[b]] == b:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica5(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == a and ladice[a] != i[0]:
                return ladice[a]
            elif ladice[ladice[b]] == b and ladice[b] != i[1]:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica6(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == a and ladice[a] != i[0] and ladice[a] != i[1]:
                return ladice[a]
            elif ladice[ladice[b]] == b and ladice[b] != i[0] and ladice[b] != i[1]:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica7(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == a and ladice[a] != i[0] and ladice[a] != i[1] and ladice[a] != ladice[b]:
                return ladice[a]
            elif ladice[ladice[b]] == b and ladice[b] != i[0] and ladice[b] != i[1] and ladice[a] != ladice[b]:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica8(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == a and ladice[a] != i[0] and ladice[a] != i[1] and ladice[a] != ladice[b] and ladice[ladice[a]] != ladice[b]:
                return ladice[a]
            elif ladice[ladice[b]] == b and ladice[b] != i[0] and ladice[b] != i[1] and ladice[a] != ladice[b] and ladice[ladice[a]] != ladice[b]:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica9(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == a and ladice[a] != i[0] and ladice[a] != i[1] and ladice[a] != ladice[b] and ladice[ladice[a]] != ladice[b] and ladice[ladice[a]] != ladice[a]:
                return ladice[a]
            elif ladice[ladice[b]] == b and ladice[b] != i[0] and ladice[b] != i[1] and ladice[a] != ladice[b] and ladice[ladice[a]] != ladice[b] and ladice[ladice[b]] != ladice[b]:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


def find_ladica_from_ladica10(ladice, i):
    a = i[0]
    b = i[1]
    while True:
        if ladice[a] == 0:
            return a
        elif ladice[b] == 0:
            return b
        else:
            if ladice[ladice[a]] == a and ladice[a] != i[0] and ladice[a] != i[1] and ladice[a] != ladice[b] and ladice[ladice[a]] != ladice[b] and ladice[ladice[a]] != ladice[a] and ladice[ladice[a]] != i[0] and ladice[ladice[a]] != i[1]:
                return ladice[a]
            elif ladice[ladice[b]] == b and ladice[b] != i[0] and ladice[b] != i[1] and ladice[a] != ladice[b] and ladice[ladice[a]] != ladice[b] and ladice[ladice[b]] != ladice[b] and ladice[ladice[b]] != i[0] and ladice[ladice[b]] != i[1]:
                return ladice[b]
            else:
                a = ladice[a]
                b = ladice[b]
                if a == b:
                    return 0
                continue


N, L = map(int, input().split())
ladice = [0] * L
for i in range(N):
    A, B = map(int, input().split())
    if find_ladica(ladice, (A, B)) != 0:
        ladica = find_ladica(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica2(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica2(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica3(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica3(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica4(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica4(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica5(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica5(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica6(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica6(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica7(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica7(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica8(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica8(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica9(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica9(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    elif find_ladica_from_ladica10(ladice, (A, B)) != 0:
        ladica = find_ladica_from_ladica10(ladice, (A, B))
        ladice[ladica] = i + 1
        print("LADICA")
        continue
    else:
        print("SMECE")
        continue