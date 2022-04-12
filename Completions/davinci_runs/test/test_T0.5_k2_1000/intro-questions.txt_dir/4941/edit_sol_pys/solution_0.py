

from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        dutch, english, correct = input().split()
        d[dutch].append((english, correct))
    correct = 0
    incorrect = 1
    for word in s:
        correct += len([c for e, c in d[word] if c == 'correct'])
        incorrect *= len([c for e, c in d[word] if c == 'incorrect'])
    print(correct + incorrect)

main()
