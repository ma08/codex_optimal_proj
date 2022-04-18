def main(b):
    if len(b) == 1:
        return b
    elif len(b) == 2:
        return b[1] + b[0]
    else:


        a = b[:2]
        for i in range(2, len(b), 2):
            a += b[i]
        return a

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
