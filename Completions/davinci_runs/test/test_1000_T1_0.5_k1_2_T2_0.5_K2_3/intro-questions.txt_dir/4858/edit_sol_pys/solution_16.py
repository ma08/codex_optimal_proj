

def main():
    m, n, c = input().split()
    m = int(m)
    n = int(n)
    first_image = []
    second_image = []
    for _ in range(m):
        first_image.append(list(input()))
    for _ in range(m):
        second_image.append(list(input()))
    for i in range(m):
        for j in range(n):
            if first_image[i][j] != c:
                first_image[i][j] = '.'
            else:
                first_image[i][j] = 'x'
            if second_image[i][j] != c:
                second_image[i][j] = '.'
            else:
                second_image[i][j] = 'x'
    for i in range(m):
        for j in range(n):
            if second_image[i][j] == 'x' and first_image[i][j] != 'x':
                second_image[i][j] = '^'
    for i in range(m):
        for j in range(n):
            if second_image[i][j] == '^':
                second_image[i][j] = '.'
            if second_image[i][j] == 'x':
                second_image[i][j] = c
    for i in range(m):
        print(''.join(second_image[i]))
    print()

if __name__ == '__main__':
    main()
