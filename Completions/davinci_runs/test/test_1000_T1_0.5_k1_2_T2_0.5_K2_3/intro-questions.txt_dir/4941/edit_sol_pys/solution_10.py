

from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        dutch, english, corr = input().split()
        d[dutch].append((english, corr))
    correct = 1
    incorrect = 0
    for w in s:
        correct *= len([c for e, c in d[w] if c == 'correct'])
        incorrect += len([c for e, c in d[w] if c == 'incorrect'])
    print(correct)
    print(incorrect)

main()
