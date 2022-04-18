

def main():
    a, b = map(int, input().split())
    if a + b <= 16:
        if (a + b) % 2 == 0:
            print("Yay!")
        else:
            print(":(")
    else:
        print(":(")
