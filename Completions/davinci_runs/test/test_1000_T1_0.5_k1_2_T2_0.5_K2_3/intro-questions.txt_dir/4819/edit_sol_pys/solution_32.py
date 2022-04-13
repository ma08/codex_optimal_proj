

def main():
    nums = [int(input()) for i in range(10)]
    print(len(set([n % 42 for n in nums])))


if __name__ == "__main__":
    main()
