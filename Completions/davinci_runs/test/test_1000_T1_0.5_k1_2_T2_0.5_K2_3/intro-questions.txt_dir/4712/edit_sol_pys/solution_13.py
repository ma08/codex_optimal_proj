
def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    print('#' * (W + 2))
    for _ in range(H):
        print('#' + a[_] + '#')
    print('#' * (W + 2))

if __name__ == '__main__':
    main()
