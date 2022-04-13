

import sys

def main():
    word = sys.stdin.readline().strip().upper()
    perm = sys.stdin.readline().strip().upper()

    # check if wins
    for i in range(len(word)):
        if word[i] not in perm[:i+1]:
            print('LOSE')
            return

    print('WIN')

main()
