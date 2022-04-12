

import collections

def main():
    n = int(input())
    dutch = input().split()
    m = int(input())
    dutch_to_english = {}
    for i in range(m):
        d, e, c = input().split()
        if d not in dutch_to_english:
            dutch_to_english[d] = {}
        if e not in dutch_to_english[d]:
            dutch_to_english[d][e] = []
        dutch_to_english[d][e].append(c)
    #print(dutch_to_english)
    english = []
    for d in dutch:
        english.append(dutch_to_english[d])
    #print(english)

    correct = 0
    incorrect = 0
    for e in english[0]['when']:
        if e == 'correct':
            correct += 1
        else:
            incorrect += 1
    for i in range(1, len(english)):
        correct_new = 0
        incorrect_new = 0
        for e in english[i]['mole']:
            if e == 'correct':
                correct_new += correct
            else:
                incorrect_new += correct
        for e in english[i]['destroy']:
            if e == 'correct':
                correct_new += incorrect
            else:
                incorrect_new += incorrect
        for e in english[i]['moles']:
            if e == 'correct':
                correct_new += incorrect
            else:
                incorrect_new += incorrect
        correct = correct_new
        incorrect = incorrect_new
    print(correct, 'correct')
    print(incorrect, 'incorrect')


if __name__ == '__main__':
    main()
