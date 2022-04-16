

def main():
    N = int(input())
    triangles = []
    for i in range(N):
        a, b, c = [int(x) for x in input().split()]
        triangles.append((a, b, c))
    print(compute_rod_length(triangles))

def compute_rod_length(triangles):
    # Write your code here
    pass

if __name__ == "__main__":
    main()
