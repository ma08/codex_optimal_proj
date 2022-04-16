

def main():
    # read input and split into a list
    N, X = [int(num) for num in input().split()]
    queue = input().split()

    # find the number of people we can let in for each gender
    num_men = [0 for _ in range(N)]
    num_women = [0 for _ in range(N)]
    for i in range(N):
        if queue[i] == 'M':
            num_men[i] = num_men[i - 1] + 1
            num_women[i] = num_women[i - 1]
        else:
            num_women[i] = num_women[i - 1] + 1
            num_men[i] = num_men[i - 1]

    # find the number of people we can let in total
    num_people = [0 for _ in range(N)]
    for i in range(N):
        if abs(num_men[i] - num_women[i]) <= X:
            num_people[i] = i + 1
        else:
            num_people[i] = num_people[i - 1]

    print(num_people[-1])

if __name__ == "__main__":
    main()
