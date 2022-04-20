
def main():
    a, b, c = [int(x) for x in input().split()]  # list comprehension
    print(max(a + b + c, 7))

if __name__ == '__main__':
    main()
