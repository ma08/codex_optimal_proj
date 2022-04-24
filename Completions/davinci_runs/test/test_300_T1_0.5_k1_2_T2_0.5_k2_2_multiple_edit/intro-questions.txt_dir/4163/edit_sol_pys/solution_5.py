# -*- coding: utf-8 -*-


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())


if __name__ == '__main__':
    main()
