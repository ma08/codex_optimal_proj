

def main(x, y, z):
    return x + y + z

if __name__ == "__main__":
    x, y = map(int, input().split())
    print(main(x, y))
