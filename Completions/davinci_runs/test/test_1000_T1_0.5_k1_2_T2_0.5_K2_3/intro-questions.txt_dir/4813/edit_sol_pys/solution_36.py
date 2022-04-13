

def main():
    word = input()
    perm = input()  # permutation
    if len(word) > len(perm):
        print("LOSE")
    else:
        print("WIN")

if __name__ == "__main__":
    main()
