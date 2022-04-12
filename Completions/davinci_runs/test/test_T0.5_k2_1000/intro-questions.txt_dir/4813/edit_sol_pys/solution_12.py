import sys

def main():
    word = sys.stdin.readline().strip().lower()
    perm = sys.stdin.readline().strip().lower()

    # check if Ned wins
    for i in range(len(word)):
        if word[i] not in perm[:i + 1]:
            print('LOSE')
            return


    print('WIN')

main()
