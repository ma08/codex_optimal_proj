

def main():
    word = input()
    if len(set(word)) < 3:
        print(0)
    else:
        print(len(word) - 2)

if __name__ == "__main__":
    main()
