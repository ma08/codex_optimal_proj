
import sys

def main():
    score = {'A': 0, 'B': 0, 'C': 0}
    for i in sys.stdin.readline().upper():
        if i == 'A' or i == 'B' or i == 'C':
            score[i] += 1 
    print(score)

if __name__ == '__main__':
    main()
