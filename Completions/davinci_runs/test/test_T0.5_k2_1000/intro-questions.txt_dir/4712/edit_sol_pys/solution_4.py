
def main():
    h, w = map(int, input().split())
    a = [list(input()) for i in range(h)]
    print('#' * (w + 2))
    for i in range(h+2):
        print('#' + a[i] + '#')
    print('#' * (w + 2))

if __name__ == '__main__':
    main()
