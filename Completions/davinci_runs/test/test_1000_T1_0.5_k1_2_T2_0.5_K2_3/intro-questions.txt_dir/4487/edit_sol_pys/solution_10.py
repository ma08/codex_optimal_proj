

def main():
    a, b, c = input().split()
    if a[-1] == b[0] and b[-1] == c[0]: # if last letter of first word is equal to first letter of second word and last letter of second word is equal to first letter of third word
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
