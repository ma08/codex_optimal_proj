
def main():
    N, B, H, W = map(int, input().split())  # N: people, B: budget, H: hotels, W: weeks
    min_cost = B  # minimum cost

    for _ in range(H):
        cost_per_person = int(input())  # cost per person
        available_beds = list(map(int, input().split()))  # available beds for each week

        for beds in available_beds:  # beds: available beds for a week
            if beds >= N:  # if there are enough beds for N people
                min_cost = min(min_cost, cost_per_person * N)  # update minimum cost

    if min_cost == B:  # if no hotel has enough beds for N people
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
