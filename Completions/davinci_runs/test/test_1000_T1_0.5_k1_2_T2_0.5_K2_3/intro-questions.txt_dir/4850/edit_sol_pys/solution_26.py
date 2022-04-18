

    # Read input
def main():
    N = int(input())
    triangles = []
    for i in range(N):
        A, B, C = [int(x) for x in input().split()]

    # Compute result
        triangles.append((A, B, C))

    print(compute_rope_length(triangles))

def compute_rope_length(triangles):
    # Write your code here
    pass


if __name__ == "__main__":
    main()
