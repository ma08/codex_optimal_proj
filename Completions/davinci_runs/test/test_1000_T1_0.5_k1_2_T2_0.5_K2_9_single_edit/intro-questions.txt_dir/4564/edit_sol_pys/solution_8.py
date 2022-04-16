def main():
    S = input()
    if len(S) == len(set(S)):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
