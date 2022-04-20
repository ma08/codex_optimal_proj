

def main():
    n = int(input())
    name = input()
    if name.count('xxx') == 0:
        print(0)
    else:
        print(n - 2)

if __name__ == "__main__":
    main()