
def main():
    N, B, H, W = map(int, input().split()) # N: number of people, B: budget, H: number of hotels, W: number of weeks
    min_cost = B # the minimum cost to book

    for _ in range(H):
        cost_per_person = int(input()) # cost per person
        available_beds = list(map(int, input().split())) # number of available beds for the week

        for beds in available_beds:
            if beds >= N: # if there is enough beds for the people
                min_cost = min(min_cost, cost_per_person * N)

    if min_cost == B: # if the minimum cost is equal to the budget, then they have to stay home
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
