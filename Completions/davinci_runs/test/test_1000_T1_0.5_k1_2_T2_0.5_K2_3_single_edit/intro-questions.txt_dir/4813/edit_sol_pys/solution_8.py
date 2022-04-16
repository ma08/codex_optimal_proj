

import sys

def main():
    word = input().strip()
    perm = input().strip()

    # check if Ned wins
    for i in range(len(word)):
        if word[i] not in perm[:i+1]:
            print('LOSE')
            return

    print('WIN')

main()
