
import sys

def main():
    score = {'A': 0, 'B': 0, 'C': 0}
    while True:
        score['A'] = 0
        score['B'] = 0
        score['C'] = 0
        for i in sys.stdin.readline().strip():
            if i == 'A' or i == 'B':
                score[i] += 1
            if score['A'] == 11 and score['B'] == 10:
                score['A'] -= 1
            if score['B'] == 11 and score['A'] == 10:
                score['B'] -= 1
            if score['A'] >= 11 and score['B'] < score['A'] - 1:
                print('A')
                break
            if score['B'] >= 11 and score['A'] < score['B'] - 1:
                print('B')
                break
        else:
            print('C')

if __name__ == '__main__':
    main()
