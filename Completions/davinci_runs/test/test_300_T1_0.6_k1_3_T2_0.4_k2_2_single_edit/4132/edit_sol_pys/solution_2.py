
def main():
    n = int(input())
    values = sorted(map(int, input().split()))
    last = values.pop(0)
    while len(values) > 0:
        last = max(last - values.pop(0), 1)
    print(last)


if __name__ == "__main__":
    main()
