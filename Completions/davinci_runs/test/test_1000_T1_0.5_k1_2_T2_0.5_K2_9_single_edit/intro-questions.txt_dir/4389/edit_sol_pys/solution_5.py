

def main(b):
    if len(b) != 2:
        a = b[:2]
        for i in range(2, len(b), 2):
            a += b[i]
        b = a
    return b

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
