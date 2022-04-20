#!/usr/bin/env python3

def main():
    n = int(input())
    skills = sorted(list(map(int, input().split())))
    max_team_size = 1
    for i in range(n - 1):
        if skills[i + 1] - skills[i] <= 5:
            max_team_size += 1
    print(max_team_size)

if __name__ == '__main__':
    main()
