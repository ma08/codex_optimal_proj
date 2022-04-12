import sys

def main():
    words = sys.stdin.readline().strip().split()
    words_set = set()
    for word in words:
        if word in words_set:
            print('no')
            return
        words_set.add(word)
    print('yes')

if __name__ == '__main__':
    main()
