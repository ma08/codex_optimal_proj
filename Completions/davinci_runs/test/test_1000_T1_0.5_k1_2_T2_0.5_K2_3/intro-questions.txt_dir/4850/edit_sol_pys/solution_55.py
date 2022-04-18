

def main():
    N = int(input())
    triangles = []
    for i in range(N):
        A, B, C = [int(x) for x in input().split()]
        triangles.append((A, B, C))
    print(compute_triangle_area(triangles, N))

def compute_triangle_area(triangles, N):
    # Write your code here
    pass

if __name__ == "__main__":
    main()
