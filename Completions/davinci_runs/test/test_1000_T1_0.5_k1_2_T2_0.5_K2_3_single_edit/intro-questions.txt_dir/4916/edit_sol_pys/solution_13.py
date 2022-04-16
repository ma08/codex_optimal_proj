

def get_min_dist(n, k, matrix, dp):
    # Implement your solution here
    return -1

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().split()])
    dp = [[-1 for i in range(n)] for j in range(n)]
    print(get_min_dist(n, k, matrix, dp))
