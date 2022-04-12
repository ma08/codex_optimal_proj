import itertools

def weight_of_word(l, w):
    letters = "abcdefghijklmnopqrstuvwxyz"
    weights = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
    ]
    combinations = itertools.combinations(letters, l)
    for c in list(combinations):
        if sum(weights[ord(x) - 97] for x in c) == w:
            return "".join(c)
    return "impossible"


l, w = [int(x) for x in input().split()]
print(weight_of_word(l, w))
