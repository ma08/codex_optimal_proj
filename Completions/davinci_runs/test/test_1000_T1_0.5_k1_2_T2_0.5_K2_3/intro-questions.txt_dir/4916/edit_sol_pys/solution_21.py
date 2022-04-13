

def get_min_dist(mat):
    # Implement your solution here
    return -1

if __name__ == "__main__":
    n = int(input())
    mat = []
    for i in range(n):
        mat.append([int(x) for x in input().split()])
    print(get_min_dist(mat))
