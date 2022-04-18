# abc166d


def main():
    x = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == x:
                print(a, b)
                return


if __name__ == '__main__':
    main()
