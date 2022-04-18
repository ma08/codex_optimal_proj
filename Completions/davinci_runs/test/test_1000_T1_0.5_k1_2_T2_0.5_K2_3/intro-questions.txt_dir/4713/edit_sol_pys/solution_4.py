

# input
def main():
    n = int(input())
# initialize
    s = input()
    x = 0
# loop
    max_x = 0
    for i in range(n):
        if s[i] == 'I':
            x += 1
        else:
# update
            x -= 1
# output
        max_x = max(max_x, x)
    print(max_x)

if __name__ == '__main__':
    main()
