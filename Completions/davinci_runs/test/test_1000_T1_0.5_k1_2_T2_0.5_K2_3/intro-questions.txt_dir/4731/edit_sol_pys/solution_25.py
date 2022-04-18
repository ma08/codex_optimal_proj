
import sys, os

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            words = line.strip().split()
            if len(words) == 1:
                return
            elif words[1][0] != words[0][-1] or words[1][0] == words[0][0]:
                print('Player 1 lost')
                return
            else:
                for i in range(1, len(words) - 1):
                    if words[i + 1][0] != words[i][-1] or words[1][0] == words[0][0]:
                        print('Player %d lost' % (i % 2 + 1))
                        return
            print('Fair Game')

if __name__ == '__main__':
    main()
