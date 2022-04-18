

import sys

def main():
    score = {'A': 0, 'B': 0}
    for i in sys.stdin.readline().strip():
        if i == 'A' or i == 'B':
            score[i] += 1
        if score['A'] == 11 and score['B'] == 10: #if A is winning by 1, B gains a point
            score['A'] -= 1
        if score['B'] == 11 and score['A'] == 10: #if B is winning by 1, A gains a point
            score['B'] -= 1
        if score['A'] >= 11 and score['B'] < score['A'] - 1: #if A is winning by 2, A wins
            print('A')
            break
        if score['B'] >= 11 and score['A'] < score['B'] - 1: #if B is winning by 2, B wins
            print('B')
            break

if __name__ == '__main__':
    main()
