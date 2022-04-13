


from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        english, dutch, correct = input().split()
        d[dutch].append((english, 'correct' if correct == 'T' else 'incorrect'))
    correct = 0
    incorrect = 1
    for word in s:
        correct += len([c for e, c in d[word] if c == 'correct'])
        incorrect *= len([c for e, c in d[word] if c == 'incorrect'])
    print(correct)
    print(incorrect)


main()
