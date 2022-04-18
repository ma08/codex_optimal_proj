

def main(b):
    return b[::2]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
