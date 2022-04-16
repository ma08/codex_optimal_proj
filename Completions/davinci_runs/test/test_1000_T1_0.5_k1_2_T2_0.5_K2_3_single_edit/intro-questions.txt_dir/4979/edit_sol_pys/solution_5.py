
def reverse(n):
    return int(bin(n)[2:][::-1],2)

if __name__ == "__main__":
    print(reverse(int(input())))
