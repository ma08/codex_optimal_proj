
import sys


def main():
    S = input()
    if len(S) == len(set(S)):  # set()は重複を削除する
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()
