

def main():
    m = input()
    r = int(len(m) ** 0.5) + 1
    while r > 0:
        c = int(len(m) // r)
        if len(m) % r == 0:
            for i in range(c):
                print(m[i::c], end="")
            break
        r -= 1

if __name__ == "__main__":
    main()
