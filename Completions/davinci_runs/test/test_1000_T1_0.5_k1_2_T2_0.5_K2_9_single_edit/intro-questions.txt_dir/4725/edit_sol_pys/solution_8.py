

def main():
    word = input().strip()
    if len(set(word)) <= 2:
        print(0)
    else:
        print(len(word) - 2)

if __name__ == "__main__":
    main()
