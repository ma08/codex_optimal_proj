

def main(x, y): 
    return "Yes" if (x + y) % 2 == 0 else "No"

if __name__ == "__main__":
    x, y = map(int, input().split())
    print(main(x, y))
