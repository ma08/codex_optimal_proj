

def main(b):
    if len(b) == 2:
        return ''.join(b)
    else:
        a = b[:2]
        for i in range(2, len(b), 2):
            a += b[i]
        return ''.join(a)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
