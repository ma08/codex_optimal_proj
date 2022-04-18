



def main():
    num = input()
    num = [int(i) for i in num]
    if next_permutation(num):
        print("".join([str(i) for i in num]))
    else:
        print("0")

if __name__ == "__main__":
    main()
