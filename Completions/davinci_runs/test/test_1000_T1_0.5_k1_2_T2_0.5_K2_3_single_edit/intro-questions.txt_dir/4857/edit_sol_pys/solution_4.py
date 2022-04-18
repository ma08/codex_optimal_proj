import itertools

def weight_of_words(l,w):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    weights = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    for i in range(1,l):
        combinations = itertools.combinations(letters,i)
        for c in combinations:
            if sum(weights[ord(x)-97] for x in c) == w:
                return c
    return 'impossible'

l,w = [int(x) for x in input().split()]
print(''.join(weight_of_words(l,w)))
