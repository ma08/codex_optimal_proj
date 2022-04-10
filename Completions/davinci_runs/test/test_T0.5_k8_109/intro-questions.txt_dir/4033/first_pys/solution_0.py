

def main(a, b):
    if a == b:
        return (a+b)*2
    if a > b:
        return main(b, a)

    # a < b
    if a*2 > b:
        return main(b-a, a) + a*2
    else:
        return main(b-a*2, a*2) + a*2

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(main(a, b))