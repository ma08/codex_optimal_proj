

def main():
    n = input().rstrip()
    n = n.split('-')
    for i in n:
        print(i[0], end="")
    print()

if __name__ == "__main__":
    main()
