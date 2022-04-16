
import sys

def main():
    word = sys.stdin.readline().strip()
    perm = sys.stdin.readline().strip()

    # check if Ned wins
    for i in range(len(word)):
        if word[i] not in perm[:i+1]:
            print('LOSE')
            return

    print('WIN')

main()
