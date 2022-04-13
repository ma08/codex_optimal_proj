
from sys import stdin
from collections import Counter
from itertools import combinations

def min_max_wins(n, a, b):
    cnt_a = Counter(a)  # count occurences of each letter in a
    cnt_b = Counter(b)  # count occurences of each letter in b
    w_a = 0  # number of wins for a
    w_b = 0  # number of wins for b
    for k, v in cnt_a.items():  # for each letter in a
        if k == "R":  # if letter is R
            w_a += min(v, cnt_b["S"])  # wins for a is min of a's R and b's S
            w_b += min(v, cnt_b["P"])  # wins for b is min of a's R and b's P
        elif k == "S":  # if letter is S
            w_a += min(v, cnt_b["P"])  # wins for a is min of a's S and b's P
            w_b += min(v, cnt_b["R"])  # wins for b is min of a's S and b's R
        elif k == "P":  # if letter is P
            w_a += min(v, cnt_b["R"])  # wins for a is min of a's P and b's R
            w_b += min(v, cnt_b["S"])  # wins for b is min of a's P and b's S
    return w_a, w_a + n - w_b  # return min and max wins

def main():
    n = int(stdin.readline().strip())  # number of rounds
    a = stdin.readline().strip().split(" ")  # a's plays
    b = stdin.readline().strip().split(" ")  # b's plays
    print(" ".join(map(str, min_max_wins(n, a, b))))  # print min and max wins

if __name__ == "__main__":
    main()
