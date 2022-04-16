

def main(a):
    b = ""
    for i in range(0, len(a), 2):
        b += a[i]
    return b

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
