
def main():
    a,b = map(int, input().split())
    a_1 = a + b
    a_2 = a - b
    a_3 = a * b
    print(max(a_1, a_2, a_3))


if __name__ == "__main__":
    main()
