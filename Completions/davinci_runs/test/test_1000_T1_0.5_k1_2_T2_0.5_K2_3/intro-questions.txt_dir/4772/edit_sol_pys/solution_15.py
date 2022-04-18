
def main():
    n, m = map(int, input().split())
    puzzle = [input() for i in range(n)]
    words = []
    for i in range(n):
        word = ''
        for j in range(m):
            if puzzle[i][j].isalpha():
                word += puzzle[i][j]
            else:
                if len(word) > 1:
                    words.append(word)
                word = ''
        if len(word) > 1:
            words.append(word)
    for j in range(m):
        word = ''
        for i in range(n):
            if puzzle[i][j].isalpha():
                word += puzzle[i][j]
            else:
                if len(word) > 1:
                    words.append(word)
                word = ''
        if len(word) > 1:
            words.append(word)
    words.sort()
    print(words[0])

if __name__ == '__main__':
    main()
