
import sys

def slugging_percentage(at_bats):
    total_bases = 0
    total_at_bats = 0
    for ab in at_bats:
        if ab > 0:
            total_bases += ab
            total_at_bats += 1
    return total_bases / total_at_bats

def main():
    n = int(sys.stdin.readline().strip())
    at_bats = list(map(int, sys.stdin.readline().strip().split()))
    print(slugging_percentage(at_bats))

if __name__ == '__main__':
    main()
