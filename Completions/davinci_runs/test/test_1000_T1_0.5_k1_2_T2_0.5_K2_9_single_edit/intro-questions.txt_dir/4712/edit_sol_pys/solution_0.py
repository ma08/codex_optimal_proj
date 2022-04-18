

def main():
    h, w = map(int, input().split())
    a = [input() for i in range(h)]
    print('#'*(w+2))  # 横線を引く
    for i in range(h):
        print('#' + a[i] + '#')
    print('#'*(w+2))  # 横線を引く

if __name__ == '__main__':
    main()
