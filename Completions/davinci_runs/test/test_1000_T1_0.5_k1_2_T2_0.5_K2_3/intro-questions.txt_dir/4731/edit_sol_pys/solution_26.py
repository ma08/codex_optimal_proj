

import sys

def main():
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    if len(words) == 1:
        return
    if words[1][0] != words[0][-1]:
        print('Player 1 lost') # wrong spelling
        return
    else:
        for i in range(1, len(words) - 1):
            if words[i + 1][0] != words[i][-1]:
                print('Player %d lost' % (i % 2 + 1)) # wrong spelling
                return
    print('Fair Game')

if __name__ == '__main__':
    main()
