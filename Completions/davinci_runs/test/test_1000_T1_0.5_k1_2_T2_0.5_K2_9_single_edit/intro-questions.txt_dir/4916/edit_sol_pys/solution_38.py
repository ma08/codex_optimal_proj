

def get_min_dist(n, k, matrix):
    # Implement your solution here
    return -1

if __name__ == "__main__":
    n, k = [int(x) for x in input().split(",")]
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().split(",")])
    print(get_min_dist(n, k, matrix))
