

def main(a):
    if len(a) == 2:
        return a[0]
    else:
        b = a[:2]
        for i in range(2, len(a), 2):
            b += a[i]
        return b[0]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
