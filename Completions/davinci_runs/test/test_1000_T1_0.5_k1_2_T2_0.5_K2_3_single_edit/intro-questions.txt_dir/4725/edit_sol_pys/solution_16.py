

def main():
    word = input()
    print(len(word) - 2 if len(set(word)) > 2 else 0)

if __name__ == "__main__":
    main()
