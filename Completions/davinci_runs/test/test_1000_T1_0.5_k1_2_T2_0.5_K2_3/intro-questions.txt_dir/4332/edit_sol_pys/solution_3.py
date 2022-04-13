def main():
    N = int(input())
    if N % sum([int(x) for x in list(str(N))]) == 0:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
