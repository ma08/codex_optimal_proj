


def get_sum(a, b):
    return a + b

def main():
    a, b = map(int, input().split())
    if get_sum(a, b) <= 16:
        if get_sum(a, b) % 2 == 0:
            print("Yay!")
        else:
            print(":(")
    else:
        print(":(")

if __name__ == "__main__":
    main()
