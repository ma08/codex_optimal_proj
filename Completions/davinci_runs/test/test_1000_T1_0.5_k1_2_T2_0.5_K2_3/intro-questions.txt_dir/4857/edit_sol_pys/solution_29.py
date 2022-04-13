import time
import itertools
start = time.time()

def weight_of_word(l,w):
    letters = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    combinations = itertools.combinations_with_replacement(letters,l)
    for c in combinations: 
        if sum(c) == w:
            return ''.join(chr(x+96) for x in c)
    return 'impossible'

l,w = [int(x) for x in input().split()]
print(weight_of_word(l,w))
print(time.time()-start)
