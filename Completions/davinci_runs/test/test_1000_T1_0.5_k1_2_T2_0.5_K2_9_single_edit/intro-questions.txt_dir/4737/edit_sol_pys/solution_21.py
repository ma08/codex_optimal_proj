def main():
    n = int(input())
    l = [int(input()) for _ in range(n)]
    l.sort()
    print(l[-1] - l[0])



if __name__ == "__main__":
    main()
