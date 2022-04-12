

from sys import stdin
from collections import defaultdict
from itertools import permutations

def main():
    n = int(stdin.readline())
    sentence = stdin.readline().rstrip().split()
    m = int(stdin.readline())
    dictionary = defaultdict(list)
    for _ in range(m):
        dutch, english, correct = stdin.readline().rstrip().split()
        dictionary[dutch].append((english, correct))
    
    if all(len(dictionary[word]) == 1 for word in sentence):
        print(' '.join(dictionary[word][0][0] for word in sentence))
        print('{} correct'.format(dictionary[word][0][1]))
    else:
        correct = 0
        incorrect = 0
        for permutation in permutations(sentence):
            if all(len(dictionary[word]) == 1 for word in permutation):
                correct += 1
            else:
                incorrect += 1
        print('{} correct'.format(correct))
        print('{} incorrect'.format(incorrect))

main()
