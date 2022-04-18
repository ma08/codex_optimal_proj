

def main():
    n = int(input())
    canisters = list(map(int, input().split()))
    canisters.sort()
    print(canisters)

if __name__ == "__main__":
    main()
