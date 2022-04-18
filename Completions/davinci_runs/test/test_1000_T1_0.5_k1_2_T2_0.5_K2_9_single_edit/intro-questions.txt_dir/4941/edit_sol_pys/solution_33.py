

from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        dutch, english, correct = input().split()
        d[dutch].append((english, correct))
    correct = 1
    incorrect = 0
    for word in s:
        correct *= len([c for e, c in d[word] if c == 'correct']) + 1
        incorrect += len([c for e, c in d[word] if c == 'incorrect']) + 1
    print(correct)
    print(incorrect)

main()
