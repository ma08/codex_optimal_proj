

import sys

def main():
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    if len(words) == 1:
        return
    elif words[1][0] != words[0][-1] or words[1][0] == words[0][0] or words[1][-1] != words[2][0]:
        print('Player 1 lost')
        return
    else:
        for i in range(1, len(words) - 1):
            if words[i + 1][0] != words[i][-1] or words[i + 1][0] == words[i][0] or words[i][-1] != words[i + 2][0]:
                print('Player %d lost' % (i % 2 + 1))
                return
    print('Fair Game')

if __name__ == '__main__':
    main()
