

def main():
    """
    Vova's Wall
    """
    n_parts = int(input())
    heights = list(map(int, input().split()))
    # print(n_parts, heights)
    # print(max(heights) - min(heights))
    if max(heights) - min(heights) > 1:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()