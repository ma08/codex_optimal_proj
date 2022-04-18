

def main():
    n = int(input())
    d = list(map(int, input().split()))

    # build array of people in order
    people = [0] * n
    for i in range(1, n):
        people[d[i-1]] = i

    # print people
    print(*people)

if __name__ == "__main__":
    main()
