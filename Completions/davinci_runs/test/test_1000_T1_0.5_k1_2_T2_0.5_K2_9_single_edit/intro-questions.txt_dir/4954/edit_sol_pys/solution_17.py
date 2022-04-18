

def main():
    N, B, H, W = map(int, input().split())  # N is number of people, B is budget, H is number of hotels, W is number of weeks
    min_cost = B  # min cost to pay

    for _ in range(H):
        cost_per_person = int(input())
        available_beds = list(map(int, input().split()))  # list of available beds in each week

        for beds in available_beds:
            if beds >= N:  # if there are enough beds
                min_cost = min(min_cost, cost_per_person * N)  # find the minimum cost

    if min_cost == B:
        print("stay home")  # if there is no hotel with enough beds
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
