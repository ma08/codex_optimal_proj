
def main():
    n = int(input())
    s = input()
    x = 0
    max_x = 0
    for i in range(n):
        if s[i] == 'I':
            x += 1
        else:
            x -= 1
        max_x = max(max_x, x)
    print(max_x)

if __name__ == '__main__':
    main()
