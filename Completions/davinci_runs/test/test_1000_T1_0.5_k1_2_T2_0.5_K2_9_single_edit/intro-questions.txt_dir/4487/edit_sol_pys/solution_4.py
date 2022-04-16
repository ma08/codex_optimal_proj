

def main():
    a, b, c = input().split()  # input a, b and c
    if a[-1] == b[0] and b[-1] == c[0]:  # check if the last letter of a is the same as the first letter of b, and the last letter of b is the same as the first letter of c
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
