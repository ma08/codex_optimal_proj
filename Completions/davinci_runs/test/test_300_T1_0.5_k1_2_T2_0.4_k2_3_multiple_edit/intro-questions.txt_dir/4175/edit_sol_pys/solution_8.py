import sys

def main():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    for i in range(N):
        if i == 0:
            pass
        else:
            if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
                print('No')
                sys.exit()

    print('Yes')

if __name__ == '__main__':
    main()
