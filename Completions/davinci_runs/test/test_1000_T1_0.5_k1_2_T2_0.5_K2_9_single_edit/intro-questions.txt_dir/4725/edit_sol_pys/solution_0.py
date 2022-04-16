

def main():
    word = input().strip()
    if len(set(word)) == 1:
    elif len(set(word)) == 2:
        if word[0] == word[-1]:
            print(len(word) - 2)
        else:
            print(len(word))
        print(0)
    else:
        print(len(word) - 2)

if __name__ == "__main__":
    main()
