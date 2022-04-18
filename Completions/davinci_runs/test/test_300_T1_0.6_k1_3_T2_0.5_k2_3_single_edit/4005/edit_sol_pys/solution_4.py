

def main():
    x1, y1, x2, y2 = [int(i) for i in input().split()]
    x3, y3, x4, y4 = [int(i) for i in input().split()]
    x5, y5, x6, y6 = [int(i) for i in input().split()]
    print("YES" if x1 >= x4 or x3 >= x2 or y1 >= y4 or y3 >= y2 else "NO")
    print("YES" if x1 >= x6 or x5 >= x2 or y1 >= y6 or y5 >= y2 else "NO")

if __name__ == "__main__":
    main()
