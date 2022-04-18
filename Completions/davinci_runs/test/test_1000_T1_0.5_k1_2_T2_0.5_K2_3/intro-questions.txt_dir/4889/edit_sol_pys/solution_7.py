
import sys

def main():
    n = int(sys.stdin.readline())
    people = []
    for i in range(n):
        people.append(int(sys.stdin.readline()))
    people.sort()
    total = people[0]
    for i in range(1, n):
        total += people[i]-1
    print(total)

if __name__ == '__main__':
    main()
