

def solver(n):
    if n % 2 == 0:
        return "White"
    else:
        return "Black"


if __name__ == "__main__":
    n = int(input())
    print(solver(n))
