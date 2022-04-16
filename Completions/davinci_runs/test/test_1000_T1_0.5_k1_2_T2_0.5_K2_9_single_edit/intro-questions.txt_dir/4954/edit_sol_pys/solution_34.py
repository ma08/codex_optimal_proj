

def main():
    N, B, H, W = map(int, input().split())
    min_cost = 100000000
    for _ in range(H):
        cost = int(input())
        num_beds = list(map(int, input().split()))
        for i in range(len(num_beds)):
            if num_beds[i] >= N and cost*N <= B:
                min_cost = min(min_cost, cost*N)
    if min_cost != 100000000:
        print(min_cost)
    else:
        print("stay home")

main()
