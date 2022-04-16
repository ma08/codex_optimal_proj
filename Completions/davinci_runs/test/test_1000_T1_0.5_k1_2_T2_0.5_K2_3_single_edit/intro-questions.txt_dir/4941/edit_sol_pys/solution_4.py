from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        dutch, english, correct = input().split()
        d[dutch].append((english, correct))
    correct_count = 1
    incorrect_count = 0
    for word in s:
        correct_count *= len([c for e, c in d[word] if c == 'correct'])
        incorrect_count += len([c for e, c in d[word] if c == 'incorrect'])
    print(correct_count)
    print(incorrect_count)

main()
