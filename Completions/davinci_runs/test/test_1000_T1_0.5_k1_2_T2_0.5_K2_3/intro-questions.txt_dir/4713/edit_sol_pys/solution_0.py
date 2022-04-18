
def main(n, s):
    x, max_x = 0, 0
    for i in s:
        x += 1 if i == 'I' else -1
        max_x = max(x, max_x)
    return max_x

if __name__ == '__main__':
    main()
