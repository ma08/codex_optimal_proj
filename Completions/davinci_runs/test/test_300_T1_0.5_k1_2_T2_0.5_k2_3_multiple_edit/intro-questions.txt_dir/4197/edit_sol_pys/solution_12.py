

def main():
    print(' '.join(map(str, sorted(enumerate(map(int, input().split()), 1), key=lambda x: x[1])[::-1])))


if __name__ == '__main__':
    main()
