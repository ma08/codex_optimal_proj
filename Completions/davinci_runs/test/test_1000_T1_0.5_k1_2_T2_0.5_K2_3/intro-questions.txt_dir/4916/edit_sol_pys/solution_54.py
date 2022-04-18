

def get_max_dist(n, k, arr):
    # Implement your solution here.
    return 0

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split()])
    print(get_max_dist(n, k, arr))
