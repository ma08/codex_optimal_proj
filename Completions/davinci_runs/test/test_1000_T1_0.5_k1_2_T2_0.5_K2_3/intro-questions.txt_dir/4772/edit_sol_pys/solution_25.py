def main():
    N = int(input())
    words = [input() for _ in range(N)]

    for word in words:
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1], end="")
        else:
            print(word, end="")
        print()

if __name__ == '__main__':
    main()
