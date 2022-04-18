

from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        dutch, english, correct = input().split()
        d[dutch].append((english, correct))
    correct_answer = 1
    incorrect_answer = 0
    for word in s:
        correct_answer *= len([c for e, c in d[word] if c == 'correct'])
        incorrect_answer += len([c for e, c in d[word] if c == 'incorrect'])
    print(correct_answer)
    print(incorrect_answer)

main()
