

def main(x, y):
    if (x == 1 and y == 3) or (x == 3 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 1) or (x == 2 and y == 4) or (x == 4 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 2) or (x == 5 and y == 7) or (x == 7 and y == 5) or (x == 6 and y == 8) or (x == 8 and y == 6) or (x == 9 and y == 11) or (x == 11 and y == 9) or (x == 10 and y == 12) or (x == 12 and y == 10):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    x, y = map(int, input().split())
    print(main(x, y))
