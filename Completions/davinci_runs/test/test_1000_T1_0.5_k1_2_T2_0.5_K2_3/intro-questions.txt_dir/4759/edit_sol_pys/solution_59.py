
import sys


def slugging_percentage(bats):
    total_bases = 0
    total_at_bats = 0
    for ab in bats:
        if ab >= 0:
            total_bases += ab
            total_at_bats += 1
    return total_bases / total_at_bats


def main():
    n = int(sys.stdin.readline().strip())
    bats = list(map(int, sys.stdin.readline().strip().split()))
    print(slugging_percentage(bats))


if __name__ == '__main__':
    main()
