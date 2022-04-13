

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    print('#' * (w + 2))
    for _ in range(h):
        print('#' + a[_] + '#')
    print('#' * (w + 2))


if __name__ == '__main__':



    main()
