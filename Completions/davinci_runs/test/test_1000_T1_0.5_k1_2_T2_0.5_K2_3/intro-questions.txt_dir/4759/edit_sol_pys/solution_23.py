

from math import floor

def main():
    n = int(input())
    at_bats = input().split()

    bases = 0
    official_at_bats = 0

    for at_bat in at_bats[:n]:
        bases += int(at_bat)
        official_at_bats += 1

    slugging_percentage = bases / official_at_bats

    print(slugging_percentage)

main()
