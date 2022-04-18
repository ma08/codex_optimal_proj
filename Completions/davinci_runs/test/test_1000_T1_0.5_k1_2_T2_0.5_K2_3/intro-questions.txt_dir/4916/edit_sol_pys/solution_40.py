

def get_min_dist(n, k, mat):
    # Implement your solution here
    pass

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    mat = []
    for i in range(n):
        mat.append([int(x) for x in input().split()])
    print(get_min_dist(n, k, mat))
