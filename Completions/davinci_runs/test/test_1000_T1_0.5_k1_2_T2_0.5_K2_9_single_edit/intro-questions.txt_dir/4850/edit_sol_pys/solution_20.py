

def main():
    N = int(input())
    triangles = []
    for i in range(N):
        A, B, C = [int(x) for x in input().split()]
        triangles.append((A, B, C))
    print(compute_rod_length(triangles))

def compute_rod_length(triangles):
    # Write your code here
    return 0

if __name__ == "__main__":
    main()
