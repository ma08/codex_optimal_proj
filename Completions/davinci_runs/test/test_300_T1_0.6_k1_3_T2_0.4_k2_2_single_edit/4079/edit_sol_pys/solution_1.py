

def main():
    n = int(input())
    for i in range(n):
        word = input()
        word = list(word)
        word.sort()
        if len(word) == 1:
            print("Yes")
        elif len(word) > 1:
            for i in range(len(word) - 1):
                if word[i] == word[i + 1]:
                    print("No")
                    break
                elif ord(word[i]) + 1 == ord(word[i + 1]):
                    if i == len(word) - 2:
                        print("Yes")
                else:
                    print("No")
                    break


if __name__ == "__main__":
    main()
