

def main():
    word = input()
    if len(set(word)) <= 2:  # set(word)はwordの文字を重複を取り除いたものを返す
        print(0)
    else:
        print(len(word) - 2)

if __name__ == "__main__":
    main()
